# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.aggregates import Avg
from django.http import JsonResponse, Http404

# Create your views here.
from django.views.generic import CreateView

from locations.models import Location
from users.views import JsonDetail
from visits.models import Visit


class LocationDetail(JsonDetail):
    model = Location


def loc_avg(request, *args, **kwargs):
    if request.method == 'GET':
        return JsonResponse({'avg': Visit.objects.filter(location=kwargs['id']).aggregate(Avg('mark'))})
    else:
        raise Http404


class LocationCreate(CreateView):
    model = Location

