from django.conf.urls.defaults import patterns, include, url
from data import views

urlpatterns = patterns('',
    url(r'^item/(?P<item_id>\d+)$', views.get_item, name='get_item'),
    url(r'^scrape/(?P<store>\w+)$', views.scrape, name='scrape'),
    url(r'^catalog/(?P<store>\w+)$', views.catalog_by_store, name='catalogbystore'),
    url(r'^catalog/$', views.catalog, name='catalog'),
    url(r'^catalog1/$', views.catalog1, name='catalog1'),
)
