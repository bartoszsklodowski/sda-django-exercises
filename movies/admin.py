from django.contrib import admin
from movies.models import Movie, Country, Actor, Oscar
# Register your models here.

admin.site.register(Movie)
admin.site.register(Country)
admin.site.register(Actor)
admin.site.register(Oscar)

