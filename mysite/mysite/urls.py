from django.contrib import admin
from django.conf.urls import url, include, re_path

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^',include('homepage.urls')),
    re_path(r'^', include('myapp.urls')),




]
