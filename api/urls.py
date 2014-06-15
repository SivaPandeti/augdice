from django.conf.urls import patterns, url, include
from api import views

urlpatterns = patterns('',
    url(r'^getMarkers$', views.getMarkers, name='getMarkers'),
    url(r'^getPieData$', views.getPieData, name='getPieData'),
    url(r'^getJobsData$', views.getJobsData, name='getJobsData'),
    )
