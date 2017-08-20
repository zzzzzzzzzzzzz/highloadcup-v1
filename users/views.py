# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
import json

# Create your views here.
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import CreateView

from users.models import User


class JsonDetail(View):
    model = None

    def get_object(self, request):
        return get_object_or_404(self.model, id=self.kwargs['id'])

    def get(self, request, *args, **kwargs):
        obj = self.get_object(request)
        return self.render_to_response(obj)

    def post(self, request, *args, **kwargs):
        obj =  get_object_or_404(self.model, id=kwargs['id'])
        try:
            obj.update(**request.POST)
            return JsonResponse({})
        except self.model.ValidationError:
            return HttpResponseBadRequest()

    def render_to_response(self, context):
        return HttpResponse(self.convert_object_to_json(context),
                            content_type='application/json')

    def convert_object_to_json(self, context):
        return json.dumps(model_to_dict(context))


class UserDetail(JsonDetail):
    model = User


class UserCreate(CreateView):
    model = User
