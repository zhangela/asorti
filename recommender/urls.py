from django.conf.urls.defaults import patterns, include, url
from recommender import views

urlpatterns = patterns('',
    url(r'^getrecommendation/(?P<item_id>\d+)$', views.get_recommendation, name='getrecommendation'),
    url(r'^getrecommendationbytype/(?P<item_type>\d+)$', views.get_recommendation_by_type, name='getrecommendationbytype'),
    url(r'^userstudy1/(?P<item_id>\d+)$', views.get_associated_items, name='userstudy1'),
    )
