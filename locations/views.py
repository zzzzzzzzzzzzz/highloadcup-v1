# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time

import datetime

from django.core.exceptions import SuspiciousOperation
from django.db.models.aggregates import Avg
from django.db.models.functions import Coalesce
from django.http import JsonResponse, Http404

# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView

from locations.models import Location
from users.views import JsonDetail
from visits.models import Visit


class LocationDetail(JsonDetail):
    model = Location


def loc_avg(request, *args, **kwargs):
    if request.method == 'GET':
        location = get_object_or_404(Location, id=kwargs['id'])
        try:
            variable_params = {}
            if 'fromDate' in request.GET:
                variable_params['visited_at__gt'] = request.GET['fromDate']
            if 'toDate' in request.GET:
                variable_params['visited_at__lt'] = request.GET['toDate']
            now = int(time.time())
            if 'fromAge' in request.GET:
                variable_params['user__birth_date__lte'] = now - 365*24*60*60*int(request.GET['fromAge'])
            if 'toAge' in request.GET:
                variable_params['user__birth_date__gte'] = now - 365*24*60*60*int(request.GET['toAge'])
            if 'gender' in request.GET:
                variable_params['user__gender'] = request.GET['gender']
            return JsonResponse(Visit.objects.filter(location=location, **variable_params).aggregate(avg=Coalesce(Avg('mark'), 0.0)))
        except:
            raise SuspiciousOperation("Invalid request; see documentation for correct paramaters")
    else:
        raise Http404


class LocationCreate(CreateView):
    model = Location

