# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
import json

# Create your views here.
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import CreateView

from users.models import User


class JsonDetail(View):
    model = None

    def get_context(self, request):
        return self.model.objects.filter(id=self.kwargs['id']).values()[0]

    def get(self, request, *args, **kwargs):
        context = self.get_context(request)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        object =  get_object_or_404(self.model, id=kwargs['id'])
        try:
            object.update(**request.POST)
            return JsonResponse({})
        except self.model.ValidationError:
            return HttpResponseBadRequest()

    def render_to_response(self, context):
        return HttpResponse(self.convert_context_to_json(context),
                            content_type='application/json')

    def convert_context_to_json(self, context):
        return json.dumps(context)


class UserDetail(JsonDetail):
    model = User


class UserCreate(CreateView):
    model = User
