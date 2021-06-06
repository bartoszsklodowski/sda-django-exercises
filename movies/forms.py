from django.forms import CharField, Form, DateTimeField, ModelChoiceField, TextInput, ModelForm, IntegerField, ModelMultipleChoiceField, CheckboxSelectMultiple
from movies.models import Actor, Country, Movie, Oscar
from django.core.exceptions import ValidationError
from datetime import datetime
import pytz

class ActorForm(Form):
    name = CharField(max_length=20)
    last_name = CharField(max_length=30)
    age = IntegerField(max_value=150)

    # def clean(self):
    #     result = super().clean()
    #     if result['answer_text'].isupper():
    #         raise ValidationError("Question name cant be uppercase")
    #     return result

class ActorModelForm(ModelForm):

    class Meta:
        model = Actor
        fields = "__all__"


class CountryForm(Form):
    name = CharField(max_length=40)
    iso_code = CharField(max_length=3)


class CountryModelForm(ModelForm):

    class Meta:
        model = Country
        fields = "__all__"

class MovieForm(Form):

    class Meta:
        model = Movie
        fields = ['title', 'genre', 'year', 'actor', 'country']

    title = CharField(max_length=128)
    genre = CharField(max_length=128)
    year = IntegerField(max_value=2021)
    actor = ModelMultipleChoiceField(queryset=Actor.objects.all(), widget=CheckboxSelectMultiple)
    country = ModelChoiceField(queryset=Country.objects.all())



class MovieModelForm(ModelForm):

    class Meta:
        model = Movie
        fields = "__all__"


class OscarForm(Form):
    category =CharField(max_length=20)
    year = IntegerField(max_value=2021)
    movie = ModelChoiceField(queryset=Movie.objects.all())
    actor = ModelChoiceField(queryset=Actor.objects.all())


class OscarModelForm(ModelForm):

    class Meta:
        model = Oscar
        fields = "__all__"