# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
import json

# Create your views here.
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from users.form import PostForm
from users.models import User


class JsonDetail(View):
    model = None

    def get_object(self, request):
        return get_object_or_404(self.model, id=self.kwargs['id'])

    def get(self, request, *args, **kwargs):
        obj = self.get_object(request)
        return self.render_to_response(obj)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, id=kwargs['id'])
        try:
            for key,value in request.POST.iteritems():
                setattr(obj, key, value)
            obj.save()
            return JsonResponse({})
        except ValueError:
            return HttpResponseBadRequest()

    def render_to_response(self, context):
        return HttpResponse(self.convert_object_to_json(context),
                            content_type='application/json')

    def convert_object_to_json(self, context):
        return json.dumps(model_to_dict(context))


@method_decorator(csrf_exempt, name='dispatch')
class UserDetail(JsonDetail):
    model = User


class MyCreateLogic(CreateView):
    def form_invalid(self, form):
        return HttpResponseBadRequest()


@method_decorator(csrf_exempt, name='dispatch')
class UserCreate(MyCreateLogic):
    model = User
    form_class = PostForm


def success(request, *args, **kwargs):
    return JsonResponse({})

