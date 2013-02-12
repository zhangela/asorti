from django.conf.urls.defaults import patterns, include, url
from data import views

urlpatterns = patterns('',
    url(r'^item/(?P<item_id>\d+)$', views.get_item, name='get_item'),
)
