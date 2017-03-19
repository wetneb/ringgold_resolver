from django.conf.urls import include, url
from django.contrib import admin
import ringgold

urlpatterns = [
    # Examples:

    url(r'^', include('ringgold.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
