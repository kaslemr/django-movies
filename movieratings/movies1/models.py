from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Movie(models.Model):
    movie = models.CharField(max_length=200)
    release_date = models.CharField(max_length=50)

    def __str__(self):
        return self.movie

class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    occupation = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return "Rater ID: {}".format(self.id)

    @property
    def raters(self):
        return self.Rating.rater_set.all().count()

class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()

    def __str__(self):
        return "{}".format(self.rater.id)

#rater.rating_set.all()


