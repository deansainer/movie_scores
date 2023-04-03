from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('series_list/', views.series_list, name='series_list'),
    path('game_list/', views.game_list, name='game_list'),
    path('api/movie_list/', views.MovieApiView.as_view()),
    path('api/series_list/', views.SeriesApiView.as_view()),
    path('api/game_list/', views.GameApiView.as_view()),
]

