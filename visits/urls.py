from django.conf.urls import url

from users.views import success
from visits.views import VisitDetail, VisitCreate

urlpatterns=[
    url(r'(?P<id>\d+)', VisitDetail.as_view(), name="detail"),
    url(r'new', VisitCreate.as_view(success_url='success/'), name="create"),
    url(r'success/$', success, name='success'),
]