#from django.conf.urls import patterns, include, url

from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Project.views.home', name='home'),
    # url(r'^Project/', include('Project.foo.urls')),
    url(r'^$', 'home.views.home', name='home'),
    url(r'^data/', include('data.urls')),
    url(r'^ratings/', include('ratings.urls')),
    url(r'^recommender/', include('recommender.urls')),
    url(r'^demo/$', 'home.views.demo', name='demo'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

try:
    from local_urls import *
    urlpatterns += url_addition
except ImportError, e:
    pass
