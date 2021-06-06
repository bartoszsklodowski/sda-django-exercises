from django.urls import path

from movies.views import actors, index_movies, countries, movies, oscars
from movies.views import ActorView, ActorTemplateView, ActorListView, CountryView, CountryTemplateView, CountryListView
from movies.views import MovieView, MovieTemplateView, MovieListView, OscarView, OscarTemplateView, OscarListView
from movies.views import actor_form, country_form, movie_form, oscar_form, ActorFormView, CountryFormView, MovieFormView, OscarFormView
from movies.views import ActorFormMethodView, CountryFormMethodView, MovieFormMethodView, OscarFormMethodView
from movies.views import ActorCreateView, CountryrCreateView, MovieCreateView, OscarCreateView
from movies.views import ActorDetailView, CountryDetailView, MovieDetailView, OscarDetailView
from movies.views import ActorGenericDetailView, CountryGenericDetailView, MovieGenericDetailView, OscarGenericDetailView
from movies.views import ActorUpdateView, CountryUpdateView, MovieUpdateView, OscarUpdateView
from movies.views import ActorGenericUpdateView, CountryGenericUpdateView, MovieGenericUpdateView, OscarGenericUpdateView
from movies.views import ActorGenericDeleteView, CountryGenericDeleteView, MovieGenericDeleteView, OscarGenericDeleteView

app_name = "movies"

urlpatterns = [
    path('', index_movies, name='index'),
    path('actors/', actors, name='actors'),
    path('countries/', countries, name='countries'),
    path('movies/', movies, name='movies'),
    path('oscars/', oscars, name='oscars'),

    path('actors-class/', ActorView.as_view(), name='actors-class'),
    path('actors-template/', ActorTemplateView.as_view(), name='actors-template'),
    path('actors-list/', ActorListView.as_view(), name='actors-list'),

    path('countries-class/', CountryView.as_view(), name='countries-class'),
    path('countries-template/', CountryTemplateView.as_view(), name='countries-template'),
    path('countries-list/', CountryListView.as_view(), name='countries-list'),

    path('movies-class/', MovieView.as_view(), name='movies-class'),
    path('movies-template/', MovieTemplateView.as_view(), name='movies-template'),
    path('movies-list/', MovieListView.as_view(), name='movies-list'),

    path('oscars-class/', OscarView.as_view(), name='oscars-class'),
    path('oscars-template/', OscarTemplateView.as_view(), name='oscars-template'),
    path('oscars-list/', OscarListView.as_view(), name='oscars-list'),

    path('my-actor-form/', actor_form),
    path('my-country-form/', country_form),
    path('my-movie-form/', movie_form),
    path('my-oscar-form/', oscar_form),

    path('my-actor-form-view/', ActorFormView.as_view(), name='actor-view'),
    path('my-country-form-view/', CountryFormView.as_view(), name='country-view'),
    path('my-movie-form-view/', MovieFormView.as_view(), name='movie-view'),
    path('my-oscar-form-view/', OscarFormView.as_view(), name='oscar-view'),

    path('my-actor-form-method-view/', ActorFormMethodView.as_view(), name = 'my-actor-form-method-view'),
    path('my-country-form-method-view/', CountryFormMethodView.as_view(), name = 'my-country-form-method-view'),
    path('my-movie-form-method-view/', MovieFormMethodView.as_view(), name = 'my-movie-form-method-view'),
    path('my-oscar-form-method-view/', OscarFormMethodView.as_view(), name = 'my-oscar-form-method-view'),

    path('actor-create-view/', ActorCreateView.as_view(), name = 'actor-create-view'),
    path('country-create-view/', CountryrCreateView.as_view(), name = 'country-create-view'),
    path('movie-create-view/', MovieCreateView.as_view(), name = 'movie-create-view'),
    path('oscar-create-view/', OscarCreateView.as_view(), name = 'oscar-create-view'),

    path('actor-detail-view/<pk>/', ActorDetailView.as_view(), name = 'actor-detail-view'),
    path('country-detail-view/<pk>/', CountryDetailView.as_view(), name = 'country-detail-view'),
    path('movie-detail-view/<pk>/', MovieDetailView.as_view(), name = 'movie-detail-view'),
    path('oscar-detail-view/<pk>/', OscarDetailView.as_view(), name = 'oscar-detail-view'),

    path('actor-generic-detail-view/<pk>/', ActorGenericDetailView.as_view(), name = 'actor-generic-detail-view'),
    path('country-generic-detail-view/<pk>/', CountryGenericDetailView.as_view(), name = 'country-generic-detail-view'),
    path('movie-generic-detail-view/<pk>/', MovieGenericDetailView.as_view(), name = 'movie-generic-detail-view'),
    path('oscar-generic-detail-view/<pk>/', OscarGenericDetailView.as_view(), name = 'oscar-generic-detail-view'),

    path('actor-update-view/<pk>/', ActorUpdateView.as_view(), name = 'actor-update-view'),
    path('country-update-view/<pk>/', CountryUpdateView.as_view(), name = 'country-update-view'),
    path('movie-update-view/<pk>/', MovieUpdateView.as_view(), name = 'movie-update-view'),
    path('oscar-update-view/<pk>/', OscarUpdateView.as_view(), name = 'oscar-update-view'),

    path('actor-generic-update-view/<pk>/', ActorGenericUpdateView.as_view(), name = 'actor-generic-update-view'),
    path('country-generic-update-view/<pk>/', CountryGenericUpdateView.as_view(), name = 'country-generic-update-view'),
    path('movie-generic-update-view/<pk>/', MovieGenericUpdateView.as_view(), name = 'movie-generic-update-view'),
    path('oscar-generic-update-view/<pk>/', OscarGenericUpdateView.as_view(), name = 'oscar-generic-update-view'),

    path('actor-delete-view/<pk>/', ActorGenericDeleteView.as_view(), name = 'actor-delete-view'),
    path('country-delete-view/<pk>/', CountryGenericDeleteView.as_view(), name = 'country-delete-view'),
    path('movie-delete-view/<pk>/', MovieGenericDeleteView.as_view(), name = 'movie-delete-view'),
    path('oscar-delete-view/<pk>/', OscarGenericDeleteView.as_view(), name = 'oscar-delete-view'),
]