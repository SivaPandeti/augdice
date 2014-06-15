from django.conf.urls import patterns, url, include
from charts import views

urlpatterns = patterns('',
    url(r'^pie$', views.pie, name='pie'),

    )
