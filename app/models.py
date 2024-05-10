from django.db import models
from datetime import date

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    
class Technician(models.Model):
    name = models.CharField(max_length=100)
    
class Movie(models.Model):
    name = models.CharField(max_length=255)
    year = models.DateField(date.today())
    rating = models.IntegerField()
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    technicians = models.ManyToManyField(Technician)
    