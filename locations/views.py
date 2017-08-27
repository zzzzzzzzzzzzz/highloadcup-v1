# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar

import datetime

from django.core.exceptions import SuspiciousOperation
from django.db.models.aggregates import Avg
from django.db.models.functions import Coalesce
from django.http import JsonResponse, Http404

# Create your views here.
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from locations.form import PostForm
from locations.models import Location
from users.views import JsonDetail, MyCreateLogic
from visits.models import Visit


@method_decorator(csrf_exempt, name='dispatch')
class LocationDetail(JsonDetail):
    model = Location


@csrf_exempt
def loc_avg(request, *args, **kwargs):
    if request.method == 'GET':
        location = get_object_or_404(Location, id=kwargs['id'])
        try:
            variable_params = {}
            if 'fromDate' in request.GET:
                variable_params['visited_at__gt'] = request.GET['fromDate']
            if 'toDate' in request.GET:
                variable_params['visited_at__lt'] = request.GET['toDate']
            now = datetime.datetime.now()
            if 'fromAge' in request.GET:
                variable_params['user__birth_date__lt'] = calendar.timegm(
                    (now - relativedelta(years=int(request.GET['fromAge']))).timetuple())
            if 'toAge' in request.GET:
                variable_params['user__birth_date__gt'] = calendar.timegm(
                    (now - relativedelta(years=int(request.GET['toAge']))).timetuple())
            if 'gender' in request.GET:
                variable_params['user__gender'] = request.GET['gender']
            return JsonResponse(
                Visit.objects.filter(location=location, **variable_params).aggregate(avg=Coalesce(Avg('mark'), 0.0)))
        except:
            raise SuspiciousOperation("Invalid request; see documentation for correct paramaters")
    else:
        raise Http404


@method_decorator(csrf_exempt, name='dispatch')
class LocationCreate(MyCreateLogic):
    model = Location
    form_class = PostForm

