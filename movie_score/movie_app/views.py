from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


def movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movie_app/movie_list.html', context)


def series_list(request):
    serieses = Series.objects.all()
    context = {'serieses': serieses}
    return render(request, 'movie_app/series_list.html', context)


def game_list(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'movie_app/game_list.html', context)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer