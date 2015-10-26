from django.shortcuts import render_to_response


# Create your views here.
from movies1.models import Movie, Rater
from django.views.generic import ListView, DetailView


def index_view(request):
    context = {}
    return render_to_response(template_name="base.html", context=context)

class MovieList(ListView):
    model = Movie
    template_name = "movie_list.html"


class MovieDetail(DetailView):
    model = Movie
    template_name = "movie_detail.html"

