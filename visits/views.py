# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core.exceptions import SuspiciousOperation
from django.db.models.expressions import F
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView

from users.models import User
from users.views import JsonDetail, MyCreateLogic
from visits.form import PostForm
from visits.models import Visit


class VisitDetail(JsonDetail):
    model = Visit


@method_decorator(csrf_exempt, name='dispatch')
class UserVisits(ListView):
    model = Visit

    def get_queryset(self):
        variable_params = {}
        user = get_object_or_404(User, id=self.kwargs['id'])
        if 'fromDate' in self.request.GET:
            variable_params['visited_at__gt'] = self.request.GET['fromDate']
        if 'toDate' in self.request.GET:
            variable_params['visited_at__lt'] = self.request.GET['toDate']
        if 'country' in self.request.GET:
            variable_params['location__country'] = self.request.GET['country']
        if 'toDistance' in self.request.GET:
            variable_params['location__distance__lt'] = self.request.GET['toDistance']
        try:
            return Visit.objects.filter(user=user, **variable_params).values('mark', 'visited_at', place=F('location__place'))
        except:
            raise SuspiciousOperation("Invalid request; see documentation for correct paramaters")

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(self.convert_context_to_json(context),
                            content_type='application/json')

    def convert_context_to_json(self, context):
        return json.dumps({'visits': list(self.object_list)})


@method_decorator(csrf_exempt, name='dispatch')
class VisitCreate(MyCreateLogic):
    model = Visit
    form_class = PostForm

