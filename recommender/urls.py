from django.conf.urls.defaults import patterns, include, url
from recommender import views

urlpatterns = patterns('',
    url(r'^getrecommendation/(?P<item_id>\d+)$', views.get_recommendation, name='getrecommendation'),
    url(r'^getrecommendationbytype/(?P<item_type>\d+)$', views.get_recommendation_by_type, name='getrecommendationbytype'),
    )
