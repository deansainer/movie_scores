from django.urls import path, include
from . import views
from .views import *


router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'series', SeriesViewSet)
router.register(r'games', GameViewSet)

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('series_list/', views.series_list, name='series_list'),
    path('game_list/', views.game_list, name='game_list'),
    path('api/', include(router.urls)),
]

