from django.contrib import admin
from .models import *


admin.site.register(Movie)
admin.site.register(MovieGenre)
admin.site.register(MovieScore)
admin.site.register(Series)
admin.site.register(SeriesGenre)
admin.site.register(SeriesScore)