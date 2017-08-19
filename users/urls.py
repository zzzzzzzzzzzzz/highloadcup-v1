from django.conf.urls import url

from users.views import UserDetail
from visits.views import UserVisits

urlpatterns=[
    url(r'(?P<id>\d+)$', UserDetail.as_view(), name="detail"),
    url(r'(?P<id>\d+)/visits$', UserVisits.as_view(), name="visits"),
]