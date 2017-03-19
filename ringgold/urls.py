from django.conf.urls import url
from .views import home, get_record

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^get$', get_record, name='get_record'),
]
