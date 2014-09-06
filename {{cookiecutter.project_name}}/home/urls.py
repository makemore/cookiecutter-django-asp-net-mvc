from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
    #runs from the root url conf only, don't duplicate the home page here
    #url(r'^$', views.index, name='index'),
    #you would probably want to run this about page directly in the root as well
    url(r'^about', views.about, name='about')
)