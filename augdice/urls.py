from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mapview.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^mapview/', include('mapview.urls', namespace="mapview")),
    url(r'^api/', include('api.urls', namespace="api")),
    url(r'^charts/', include('charts.urls', namespace="charts")),
    #url(r'^ingest/', include('ingest.urls', namespace="ingest")),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    #url(r'^$', include('mapview.urls', namespace="mapview")),
)
