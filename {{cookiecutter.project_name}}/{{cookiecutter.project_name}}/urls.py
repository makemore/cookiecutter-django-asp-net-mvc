from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    url(r'^home/', include('home.urls')),
    (r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.ico'))
)