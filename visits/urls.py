from django.conf.urls import url

from visits.views import VisitDetail

urlpatterns=[
    url(r'(?P<id>\d+)$', VisitDetail.as_view(), name="detail"),
]