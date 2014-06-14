from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mapview.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^mapview/', include('mapview.urls', namespace="mapview")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('mapview.urls', namespace="mapview")),
)
