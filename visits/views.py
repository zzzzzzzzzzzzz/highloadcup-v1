# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView

from users.views import JsonDetail
from visits.models import Visit


class VisitDetail(JsonDetail):
    model = Visit


class UserVisits(ListView):
    model = Visit

    def get_queryset(self):
        return Visit.objects.filter(user=self.kwargs['id']) # пока что без фильтрации по дате

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(self.convert_context_to_json(context),
                            content_type='application/json')

    def convert_context_to_json(self, context):
        return serializers.serialize("json", self.object_list)


class VisitCreate(CreateView):
    model = Visit

