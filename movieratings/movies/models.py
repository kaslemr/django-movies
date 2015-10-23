from django.db import models

# Create your models here.

class Movie(models.Model):
    movie = models.CharField(max_length=200)
    release_data = models.CharField(max_length=50)

class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    occupation = models.CharField(max_length=50)
    zip_code = models.IntegerField()




