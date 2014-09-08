from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    url(r'^home/', include('home.urls')),
    (r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)