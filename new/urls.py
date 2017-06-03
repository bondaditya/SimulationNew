from django.conf.urls import url
from django.contrib import admin

from simuli import views

from .views import (
    IntroView,

    TeamView,
    ProductView,
    ProductionView,
    SupplyView,
    BoardView,
    ResultView,
    ProductUpdateView,
    ForcastCreateView,
    SupplyCreateView,
    VendorCreateView,
    UserProfileUpdateView,
    SupplyUpdateView,
    SupplyUpdateView2,
    SupplyUpdateView3,
    SupplyUpdateView4,
    SendInvite,
    TestView,
    ReportView,

    )

urlpatterns = [
    url(r'^$', IntroView, name='intro'),
    url(r'^design$', ProductView, name='design'),
    url(r'^team', TeamView, name='team'),
    url(r'^production', ProductionView, name='production'),
    url(r'^supply$', SupplyView, name='supply'),
    url(r'^board', BoardView, name='board'),
    url(r'^result', ResultView, name='results'),
    url(r'^test', TestView, name='test'),
    url(r'^report', ReportView, name='report'),
    url(r'^invite', SendInvite.as_view(), name='invite'),

    # url(r'^videos/(?P<pk>\d+)/$', VideoDetailView.as_view(), name='video-detail'),
    #url(r'^(?P<slug>[\w-]+)/$', VideoDetailView.as_view(), name='detail'),
    url(r'^forcast/(?P<pk>[0-9]+)/', ForcastCreateView.as_view(), name='forcastupdate'),
    url(r'^createsupply$', SupplyCreateView, name='supplycreate'),
    url(r'^design/(?P<pk>[0-9]+)/', ProductUpdateView.as_view(), name='designupdate'),
    url(r'^createvendor$', VendorCreateView, name='createvendor'),
    url(r'^profile/(?P<pk>[0-9]+)/', UserProfileUpdateView.as_view(), name='profileupdate'),
    url(r'^supply/(?P<pk>[0-9]+)/', SupplyUpdateView.as_view(), name='supplyupdate'),
    url(r'^2supply/(?P<pk>[0-9]+)/', SupplyUpdateView2.as_view(), name='supplyupdate2'),
    url(r'^3supply/(?P<pk>[0-9]+)/', SupplyUpdateView3.as_view(), name='supplyupdate3'),
    url(r'^4supply/(?P<pk>[0-9]+)/', SupplyUpdateView4.as_view(), name='supplyupdate4'),
     
    #url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),  



]