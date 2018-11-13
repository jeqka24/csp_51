from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
#    path('sportsman', views.),
#    path('sportsman', views.SportsmenView.as_view(), name="sportsmen-view"),
#    path('sportsman/<int:id>/', views.SportsmanView.as_view(), name="sportsman-detail"),
#    path('sportsman', include(views.SportsmanView().urls)),
]