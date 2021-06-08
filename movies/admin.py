from django.contrib import admin
from movies.models import Movie, Country, Actor, Oscar


# Register your models here.

class ActorsAdmin(admin.ModelAdmin):
    ordering = ('name', 'last_name',)
    list_display = ('id', 'name', 'last_name', 'age', 'oscars')
    list_display_links = ('id', 'name',)
    list_per_page = 20
    search_fields = ('name', 'last_name',)

    fieldsets = [
        ('General', {
            'fields': ['name', 'last_name', 'age', ]
        }),
    ]

    readonly_fields = ['age']

    def oscars(self, obj):
        return Oscar.objects.filter(actor__name=obj.name).count()


class CountriesAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('id', 'name', 'iso_code',)
    list_display_links = ('id', 'name',)
    list_per_page = 20
    search_fields = ('name',)
    actions = ('cleanup_iso_code',)

    fieldsets = [
        ('General', {
            'fields': ['name', 'iso_code', ]
        }),
    ]

    readonly_fields = ['iso_code']

    @staticmethod
    def cleanup_iso_code(modeladmin, request, queryset):
        queryset.update(iso_code="")


class MovieAdmin(admin.ModelAdmin):
    ordering = ('title',)
    list_display = ('id', 'title', 'genre', 'year', 'oscars')
    list_display_links = ('id', 'title',)
    list_per_page = 20
    list_filter = ('year',)
    search_fields = ('title',)

    fieldsets = [
        ('General', {
            'fields': ['title', 'genre', 'year', ]
        }),
        ('External Information', {
            'fields': ['actor', 'country'],
            'description': 'Information about related actor and country'
        })
    ]

    readonly_fields = ['year']

    def oscars(self, obj):
        return Oscar.objects.filter(movie__title=obj.title).count()


class OscarAdmin(admin.ModelAdmin):
    ordering = ('year',)
    list_display = ('year', 'category', 'winner_actor', 'winner_movie',)
    list_display_links = ('year', 'category',)
    list_per_page = 20
    list_filter = ('year',)

    fieldsets = [
        ('General', {
            'fields': ['category', 'year', ]
        }),
        ('External Information', {
            'fields': ['movie', 'actor'],
            'description': 'Information about related movie and actor'
        })
    ]

    readonly_fields = ['year']

    def winner_actor(self, obj):
        queryset = Actor.objects.filter(oscar_for_actors=obj)
        if queryset:
            return f'{queryset[0].name} {queryset[0].last_name}'

    def winner_movie(self, obj):
        queryset = Movie.objects.filter(oscar_for_movies=obj)
        if queryset:
            return f'{queryset[0].title} '


admin.site.register(Movie, MovieAdmin)
admin.site.register(Country, CountriesAdmin)
admin.site.register(Actor, ActorsAdmin)
admin.site.register(Oscar, OscarAdmin)
