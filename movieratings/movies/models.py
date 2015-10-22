from django.db import models

# Create your models here.

class Movies(models.Model):
    movie_id = models.IntegerField()
    movie = models.CharField(max_length=200)
    release_data = models.DateTimeField()

    def __str__(self):
        return self.movie


class ratings(models.Model):
    user_id = models.IntegerField()
    movie_id = models.IntegerField()
    rating = models.IntegerField()
    rating_date = models.DateTimeField()


class users(models.Model):
    user_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    occupation = models.CharField(max_length=50)
    zip_code = models.IntegerField()

    def __str__(self):
        return self.user_id

