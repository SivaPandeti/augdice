from django.conf.urls import patterns, url, include
from mapview import views


urlpatterns = patterns('',
    url(r'^job$', views.job, name='job'),

    )
