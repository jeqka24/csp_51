from django.urls import path, re_path
from . import views

from django.conf.urls import url, include

urlpatterns = [
    path('', views.indexView.as_view(), name="home"),
    re_path(r'^sportsman/(?P<pk>\d+)$', views.SportsmanView.as_view(), name='sportsman-detail'),
    re_path(r'^sportsman/?$', views.SportsmenView.as_view(), name='sportsmen'),

    re_path(r'^trainer/(?P<pk>\d+)$', views.TrainerView.as_view(), name='trainer-detail'),
    re_path(r'^trainer/?$', views.TrainersView.as_view(), name='trainers'),

    re_path(r'^event/(?P<pk>\d+)$', views.EventView.as_view(), name='event-detail'),
    re_path(r'^events/?$', views.EventsView.as_view(), name='events'),

    re_path(r'^result/(?P<pk>\d+)$', views.ResultView.as_view(), name='result-detail'),
    re_path(r'^results/?$', views.ResultsView.as_view(), name='results'),

    #    path('sportsman', include(views.SportsmanView().urls)),
]
