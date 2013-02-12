from django.conf.urls.defaults import patterns, include, url
from ratings import views

urlpatterns = patterns('',
    url(r'^createandrate$', views.create_and_rate_outfit, name='createandrate'),
    url(r'^outfit/(?P<outfit_id>\d+)$', views.getoutfit, name='getoutfit'),
    url(r'^ratepair/(?P<outfit_id>\d+)$', views.ratepair, name='ratepair'),
)
