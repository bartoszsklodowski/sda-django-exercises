from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    age = models.SmallIntegerField()

    class Meta:
        ordering = ['name', 'last_name', 'age']

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Country(models.Model):
    name = models.CharField(max_length=40)
    iso_code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name}"

class Movie(models.Model):
    title = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    year = models.SmallIntegerField()
    actor = models.ManyToManyField(Actor, blank=True, related_name="movies")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, related_name="movies")

    class Meta:
        ordering = ['title', 'genre', 'year']

    def __str__(self):
        return f"{self.title}"

class Oscar(models.Model):
    category = models.CharField(max_length=20)
    year = models.SmallIntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True, related_name="oscar_for_movies")
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, null=True, blank=True, related_name="oscar_for_actors")

    def __str__(self):
        return f"{self.category} {self.year}"

