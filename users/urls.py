from django.conf.urls import url
from django.urls import reverse

from users.views import UserDetail, UserCreate, success
from visits.views import UserVisits

urlpatterns=[
    url(r'(?P<id>\d+)/$', UserDetail.as_view(), name="detail"),
    url(r'new/$', UserCreate.as_view(success_url='success/'), name="create"),
    url(r'success/$', success, name='success'),
    url(r'(?P<id>\d+)/visits/$', UserVisits.as_view(), name="visits"),
]