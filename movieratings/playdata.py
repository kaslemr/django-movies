__author__ = 'MattKasle'

import pandas as pd

def load_data_movies(apps, schema_editor):

    movies = pd.read_csv('movies1/u.item', sep="|", encoding="ISO-8859-1", header=-1)
    movies = movies.rename(columns={0:"movie_id", 1:"movie", 2:"release_date",
                                3:"video_release_date", 4:"url"})
    movies = movies[["movie_id", "movie", 'release_date']]
    movies = movies[movies.movie_id != 267]
    Movie = apps.get_model("movies1", "Movie")

    for index, row in movies.iterrows():
        movie_id = row.movie_id
        movie = row.movie
        release_date = row.release_date
        Movie.objects.create(id=movie_id, movie=movie, release_date=release_date)

#from play import load data into migration
#pas runpython function into migration

def load_data_raters(apps, schema_editor):
    raters = pd.read_csv('movies1/u.user', sep="|", encoding="ISO-8859-1", header=-1)
    raters = raters.rename(columns={0:"user_id", 1:"age", 2:"gender",
                                3:"occupation", 4:"zip_code"})
    Rater = apps.get_model("movies1", "Rater")

    for index, row in raters.iterrows():
        user_id = row.user_id
        age = row.age
        gender = row.gender
        occupation = row.occupation
        zip_code = row.zip_code
        Rater.objects.create(id=user_id, age=age, gender=gender, occupation=occupation, zip_code=zip_code)

def load_data_ratings(apps, schema_editor):
    df = pd.read_csv('movies1/u.data', sep="\t", header=-1)
    df = df.rename(columns={0:"user_id", 1:"movie_id",
                        2:"rating", 3:"timestamp"})
    df = df[["user_id", "movie_id", 'rating']]
    df = df[df.movie_id != 267]

    Rating = apps.get_model("movies1", "Rating")
    Movie = apps.get_model("movies1", "Movie")
    Rater = apps.get_model("movies1", "Rater")

    for index, row in df.iterrows():
        rater = row.user_id
        movie = row.movie_id
        rating = row.rating
        Rating.objects.create(rater=Rater.objects.get(id=rater), movie=Movie.objects.get(id=movie), rating=rating)