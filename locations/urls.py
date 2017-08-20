from django.conf.urls import url

from locations.views import LocationDetail, loc_avg

urlpatterns=[
    url(r'(?P<id>\d+)/$', LocationDetail.as_view(), name='detail'),
    url(r'(?P<id>\d+)/avg/$', loc_avg, name='avg'),
]