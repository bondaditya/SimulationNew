from django.conf.urls import url
from django.contrib import admin
from simuli import views 

from .views import (
    IntroView,

    TeamView,
    DesignView,
    ProductionView,
    SupplyView,
    BoardView,
    ResultView,
    ForcastUpdateView,
    SupplyUpdateView,
    DesignUpdateView,
    )

urlpatterns = [
    url(r'^$', IntroView, name='intro'),
    url(r'^design', DesignView, name='design'),
    url(r'^team', TeamView, name='team'),
    url(r'^production', ProductionView, name='production'),
    url(r'^supply', SupplyView, name='supply'),
    url(r'^board', BoardView, name='board'),
    url(r'^result', ResultView, name='result'),
   
    # url(r'^videos/(?P<pk>\d+)/$', VideoDetailView.as_view(), name='video-detail'),
    #url(r'^(?P<slug>[\w-]+)/$', VideoDetailView.as_view(), name='detail'),
    url(r'^(?P<id>\d+)/forcast/$', ForcastUpdateView, name='forcastupdate'),
    url(r'^(?P<id>\d+)/supply/$', SupplyUpdateView, name='supplyupdate'),
    url(r'^(?P<id>\d+)/design/$', DesignUpdateView, name='designupdate'),
    

]