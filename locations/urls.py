from django.conf.urls import url
from django.views.decorators.cache import cache_page

from locations.views import LocationDetail, loc_avg, LocationCreate
from users.views import success

urlpatterns=[
    url(r'(?P<id>\d+)/$', LocationDetail.as_view(), name='detail'),
    url(r'new/$', LocationCreate.as_view(success_url='success/'), name="create"),
    url(r'success/$', success, name='success'),
    url(r'(?P<id>\d+)/avg/$', cache_page(60*2)(loc_avg), name='avg'),
]