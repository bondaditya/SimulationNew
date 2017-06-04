from django.conf.urls import url
from django.contrib import admin

from simuli import views 
from . import views
    

urlpatterns = [
    #url(r'^', HomeView.as_view(), name='case_home'),
    url(r'^intro', views.IntroView, name='case_intro'),
    url(r'^planning', views.PlanningView, name='case_planning'),
    url(r'^supply', views.SupplyView, name='case_supply'),
    url(r'^marketing', views.MarketingView, name='case_marketing'),
    url(r'^budget', views.BudgetView, name='case_budget'),
    # url(r'^videos/(?P<pk>\d+)/$', VideoDetailView.as_view(), name='video-detail'),
    #url(r'^(?P<slug>[\w-]+)/$', VideoDetailView.as_view(), name='detai'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', VideoUpdateView.as_view(), name='update'),
    #url(r'^(?P<slug>[\w-]+)/delete/$', VideoDeleteView.as_view(), name='delete'),

]