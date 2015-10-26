from django.shortcuts import render_to_response


# Create your views here.
from movies1.models import Movie, Rater
from django.views.generic import ListView, DetailView


def index_view(request):
    context = {}
    return render_to_response(template_name="base.html", context=context)

def movie_list_view(request):
    all_movies = Movie.objects.all()
    return render_to_response(template_name="movie_list.html", context={"movie_list": all_movies})

def movie_detail_view(request, movie_id):
    movies = Movie.objects.get(id=movie_id)
    ratings = movies.rating_set.all()
    context={"movie_object": movies, "ratings": ratings}
    return render_to_response(template_name="movie_detail.html", context=context)
