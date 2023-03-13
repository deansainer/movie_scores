from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('series_list/', views.series_list, name='series_list')
]

