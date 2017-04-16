
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^[index/]*$', views.index, name='index'),
    url(r'^list/(?P<apikey>\d{6})/$',  views.list_all, name='list_all'),
    url(r'^list/(?P<apikey>\d{6})/(?P<pk>\d+)/$',  views.detail, name='detail'),
    url(r'^list/(?P<apikey>\d{6})/(?P<pk>\d+)/delete$',  views.delete, name='delete'),
    url(r'^upload/$',  views.upload, name='upload'),
    url(r'^getkey/$',  views.generate_key, name='generate_key'),
]