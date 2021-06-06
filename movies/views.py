from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, FormView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from movies.models import Actor, Country, Movie, Oscar
from movies.forms import ActorForm, ActorModelForm, CountryForm, CountryModelForm, MovieForm, MovieModelForm
from movies.forms import OscarForm, OscarModelForm

# WIDOK JAKO FUNKCJA
def hello(request):
    year = request.GET.get("year","")
    return HttpResponse(f'Hello, world! {year}')

def actors(request):
    return render(request, template_name="actors.html", context={"actors": Actor.objects.all()})

def index_movies(request):
    return render(request, template_name="index_movies.html")

def countries(request):
    return render(request, template_name="countries.html", context={"countries": Country.objects.all()})

def movies(request):
    return render(request, template_name="movies.html", context={"movies": Movie.objects.all()})

def oscars(request):
    return render(request, template_name="oscars.html", context={"oscars": Oscar.objects.all()})


# WIDOK JAKO KLASA VIEW
class ActorView(View):

    def get(self, request):
        return render(request, template_name="actors.html", context={"actors": Actor.objects.all()})

class CountryView(View):

    def get(self, request):
        return render(request, template_name="countries.html", context={"countries": Country.objects.all()})

class MovieView(View):

    def get(self, request):
        return render(request, template_name="movies.html", context={"movies": Movie.objects.all()})

class OscarView(View):

    def get(self, request):
        return render(request, template_name="oscars.html", context={"oscars": Oscar.objects.all()})

# WIDOK JAKO KLASA TEMPLATEVIEW
class ActorTemplateView(TemplateView):
    template_name = "actors.html"
    extra_context = {"actors": Actor.objects.all()}

class CountryTemplateView(TemplateView):
    template_name = "countries.html"
    extra_context = {"countries": Country.objects.all()}

class MovieTemplateView(TemplateView):
    template_name = "movies.html"
    extra_context = {"movies": Movie.objects.all()}

class OscarTemplateView(TemplateView):
    template_name = "oscars.html"
    extra_context = {"oscars": Oscar.objects.all()}

# WIDOK JAKO KLASA LISTVIEW
class ActorListView(ListView):
    template_name = "actors.html"
    model = Actor

class CountryListView(ListView):
    template_name = "countries.html"
    model = Country

class MovieListView(ListView):
    template_name = "movies.html"
    model = Movie

class OscarListView(ListView):
    template_name = "oscars.html"
    model = Oscar

# FORMULARZ PRZY UZYCIU FUNCKJI
def actor_form(request):
    form = ActorForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']
        age = form.cleaned_data['age']
        Actor.objects.create(name=name, last_name=last_name, age=age)
        return HttpResponse('ACTOR ADDED')
    return render(request, template_name='form.html', context={'form': form})

def country_form(request):
    form = CountryForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        iso_code = form.cleaned_data['iso_code']
        Country.objects.create(name=name, iso_code=iso_code)
        return HttpResponse('COUNTRY ADDED')
    return render(request, template_name='form.html', context={'form': form})

def movie_form(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data['title']
        genre = form.cleaned_data['genre']
        year = form.cleaned_data['year']
        actors = form.cleaned_data['actor']
        country = form.cleaned_data['country']
        new_movie = Movie.objects.create(title=title, genre=genre, year=year, country=country)
        for actor in actors:
            actor_object = Actor.objects.get(name=actor.name, last_name=actor.last_name)
            new_movie.actor.add(actor_object)
        return HttpResponse('MOVIE ADDED')
    return render(request, template_name='form.html', context={'form': form})

def oscar_form(request):
    form = OscarForm(request.POST or None)
    if form.is_valid():
        category = form.cleaned_data['category']
        year = form.cleaned_data['year']
        movie = form.cleaned_data['movie']
        actor = form.cleaned_data['actor']
        Oscar.objects.create(category=category, year=year, movie=movie, actor=actor)
        return HttpResponse('OSCAR ADDED')
    return render(request, template_name='form.html', context={'form': form})

# FORMULARZ PRZY UZYCIU KLASY FORMVIEW
class ActorFormView(FormView):
    template_name = "form.html"
    form_class = ActorModelForm
    success_url = reverse_lazy("movies:index")

    def form_valid(self,form):
        result = super().form_valid(form)
        name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']
        age = form.cleaned_data['age']
        Actor.objects.create(name=name, last_name=last_name, age=age)
        return result

    def form_invalid(self, form):
        return super().form_invalid(form)

class CountryFormView(FormView):
    template_name = "form.html"
    form_class = CountryModelForm
    success_url = reverse_lazy("movies:index")

    def form_valid(self,form):
        result = super().form_valid(form)
        name = form.cleaned_data['name']
        iso_code = form.cleaned_data['iso_code']
        Country.objects.create(name=name, iso_code=iso_code)
        return result

    def form_invalid(self, form):
        return super().form_invalid(form)

class MovieFormView(FormView):
    template_name = "form.html"
    form_class = MovieModelForm
    success_url = reverse_lazy("movies:index")

    def form_valid(self,form):
        result = super().form_valid(form)
        title = form.cleaned_data['title']
        genre = form.cleaned_data['genre']
        year = form.cleaned_data['year']
        actors = form.cleaned_data['actor']
        country = form.cleaned_data['country']
        new_movie = Movie.objects.create(title=title, genre=genre, year=year, country=country)
        for actor in actors:
            actor_object = Actor.objects.get(name=actor.name, last_name=actor.last_name)
            new_movie.actor.add(actor_object)
        return result

    def form_invalid(self, form):
        return super().form_invalid(form)

class OscarFormView(FormView):
    template_name = "form.html"
    form_class = OscarModelForm
    success_url = reverse_lazy("movies:index")

    def form_valid(self,form):
        result = super().form_valid(form)
        category = form.cleaned_data['category']
        year = form.cleaned_data['year']
        movie = form.cleaned_data['movie']
        actor = form.cleaned_data['actor']
        Oscar.objects.create(category=category, year=year, movie=movie, actor=actor)
        return result

    def form_invalid(self, form):
        return super().form_invalid(form)

# FORMULARZ PRZY UZYCIU KLASY VIEW
class ActorFormMethodView(View):
    def get(self, request):
        form = ActorForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )
    def post(self, request):
        form = ActorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            Actor.objects.create(name=name, last_name=last_name, age=age)
            return HttpResponseRedirect(reverse("movies:index"))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )

class CountryFormMethodView(View):
    def get(self, request):
        form = CountryForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )
    def post(self, request):
        form = CountryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            iso_code = form.cleaned_data['iso_code']
            Country.objects.create(name=name, iso_code=iso_code)
            return HttpResponseRedirect(reverse("movies:index"))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )

class MovieFormMethodView(View):
    def get(self, request):
        form = MovieForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )
    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            genre = form.cleaned_data['genre']
            year = form.cleaned_data['year']
            actors = form.cleaned_data['actor']
            country = form.cleaned_data['country']
            new_movie = Movie.objects.create(title=title, genre=genre, year=year, country=country)
            for actor in actors:
                actor_object = Actor.objects.get(name = actor.name, last_name = actor.last_name)
                new_movie.actor.add(actor_object)
            return HttpResponseRedirect(reverse("movies:index"))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )

class OscarFormMethodView(View):
    def get(self, request):
        form = OscarForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )
    def post(self, request):
        form = OscarForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            year = form.cleaned_data['year']
            movie = form.cleaned_data['movie']
            actor = form.cleaned_data['actor']
            Oscar.objects.create(category=category, year=year, movie=movie, actor=actor)
            return HttpResponseRedirect(reverse("movies:index"))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )


# FORMULARZ PRZY UZYCIU KLASY CREATEVIEW - CREATE
class ActorCreateView(CreateView):

    model = Actor
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("movies:index")

class CountryrCreateView(CreateView):

    model = Country
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("movies:index")

class MovieCreateView(CreateView):

    model = Movie
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("movies:index")

class OscarCreateView(CreateView):

    model = Oscar
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("movies:index")

# WYSWIETLANIE OBIEKTOW PRZY UZYCIU KLASY VIEW - READ
class ActorDetailView(View):
    def get(self, request, pk):
        obj = get_object_or_404(Actor, pk=pk)
        return render(
            request,
            template_name="actor.html",
            context={"actor": obj}
        )

class CountryDetailView(View):
    def get(self, request, pk):
        obj = get_object_or_404(Country, pk=pk)
        return render(
            request,
            template_name="country.html",
            context={"country": obj}
        )

class MovieDetailView(View):
    def get(self, request, pk):
        obj = get_object_or_404(Movie, pk=pk)
        return render(
            request,
            template_name="movie.html",
            context={"movie": obj}
        )

class OscarDetailView(View):
    def get(self, request, pk):
        obj = get_object_or_404(Oscar, pk=pk)
        return render(
            request,
            template_name="oscar.html",
            context={"oscar": obj}
        )

# WYSWIETLANIE OBIEKTOW PRZY UZYCIU KLASY DETAILVIEW - READ
class ActorGenericDetailView(DetailView):
    model = Actor
    template_name = "actor.html"

class CountryGenericDetailView(DetailView):
    model = Country
    template_name = "country.html"

class MovieGenericDetailView(DetailView):
    model = Movie
    template_name = "movie.html"

class OscarGenericDetailView(DetailView):
    model = Oscar
    template_name = "oscar.html"

# ZMIANA OBIEKTÓW PRZY UZYCIU KLASY VIEW - GET + POST = UPDATE
class ActorUpdateView(View):

    def get(self,request, pk):
        form = ActorForm()
        return render(request, template_name="form.html", context={"form":form})

    def post(self,request, pk):
        form = ActorForm(request.POST or None)
        if form.is_valid():
            q = get_object_or_404(Actor, pk=pk)
            q.name = form.cleaned_data["name"]
            q.last_name = form.cleaned_data["last_name"]
            q.age = form.cleaned_data["age"]
            q.save()
            return HttpResponseRedirect(reverse("movies:index_movies"))
        return render(request, template_name="form.html", context={"form": form})

class CountryUpdateView(View):

    def get(self,request, pk):
        form = CountryForm()
        return render(request, template_name="form.html", context={"form":form})

    def post(self,request, pk):
        form = CountryForm(request.POST or None)
        if form.is_valid():
            q = get_object_or_404(Country, pk=pk)
            q.name = form.cleaned_data["name"]
            q.iso_code = form.cleaned_data["iso_code"]
            q.save()
            return HttpResponseRedirect(reverse("movies:index_movies"))
        return render(request, template_name="form.html", context={"form": form})

class MovieUpdateView(View):

    def get(self,request, pk):
        form = MovieForm()
        return render(request, template_name="form.html", context={"form":form})

    def post(self,request, pk):
        form = MovieForm(request.POST or None)
        if form.is_valid():
            q = get_object_or_404(Movie, pk=pk)
            q.title = form.cleaned_data["title"]
            q.genre = form.cleaned_data["genre"]
            q.year = form.cleaned_data["year"]
            q.save()
            return HttpResponseRedirect(reverse("movies:index_movies"))
        return render(request, template_name="form.html", context={"form": form})



class OscarUpdateView(View):

    def get(self,request, pk):
        form = OscarForm()
        return render(request, template_name="form.html", context={"form":form})

    def post(self,request, pk):
        form = OscarForm(request.POST or None)
        if form.is_valid():
            q = get_object_or_404(Oscar, pk=pk)
            q.category = form.cleaned_data["category"]
            q.year = form.cleaned_data["year"]
            q.save()
            return HttpResponseRedirect(reverse("movies:index_movies"))
        return render(request, template_name="form.html", context={"form": form})


# ZMIANA OBIEKTÓW PRZY UZYCIU KLASY GENERYCZNEJ (CLASS BASED VIEW) UPDATEVIEW - GET + POST = UPDATE
class ActorGenericUpdateView(UpdateView):
    # permission_required = ['movies.view_actor', 'movies.add_actor']
    model = Actor
    fields = ("name","last_name", "age",)
    template_name = "form.html"
    success_url = reverse_lazy("movies:index_movies")

class CountryGenericUpdateView(UpdateView):
    # permission_required = ['movies.view_actor', 'movies.add_actor']
    model = Country
    fields = ("name","iso_code",)
    template_name = "form.html"
    success_url = reverse_lazy("movies:index_movies")

class MovieGenericUpdateView(UpdateView):
    # permission_required = ['movies.view_actor', 'movies.add_actor']
    model = Movie
    fields = ("title","genre", "year",)
    template_name = "form.html"
    success_url = reverse_lazy("movies:index_movies")

class OscarGenericUpdateView(UpdateView):
    # permission_required = ['movies.view_actor', 'movies.add_actor']
    model = Actor
    fields = ("category","year", )
    template_name = "form.html"
    success_url = reverse_lazy("movies:index_movies")


# USUWANIE OBIEKTÓW PRZY UZYCIU KLASY GENERYCZNEJ (CLASS BASED VIEW) DELETEVIEW - DELETE
class ActorGenericDeleteView(DeleteView):
    # permission_required = ['movies.delete_actor', ]
    model = Actor
    fields = ("name","last_name", "age",)
    template_name = "delete_form.html"
    success_url = reverse_lazy("movies:index_movies")

class CountryGenericDeleteView(DeleteView):
    # permission_required = ['movies.delete_actor', ]
    model = Country
    fields = ("name","iso_code",)
    template_name = "delete_form.html"
    success_url = reverse_lazy("movies:index_movies")

class MovieGenericDeleteView(DeleteView):
    # permission_required = ['movies.delete_actor', ]
    model = Movie
    fields = ("title", "genre", "year",)
    template_name = "delete_form.html"
    success_url = reverse_lazy("movies:index_movies")

class OscarGenericDeleteView(DeleteView):
    # permission_required = ['movies.delete_actor', ]
    model = Oscar
    fields = ("category","year", )
    template_name = "delete_form.html"
    success_url = reverse_lazy("movies:index_movies")