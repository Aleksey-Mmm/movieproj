from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.shortcuts import get_object_or_404


# Create your views here.

def home(request):
    search_term = request.GET.get('searchMovie')
    if search_term:
        movies = Movie.objects.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()

    return render(request, 'home.html',
                  {'searchTerm': search_term, 'movies': movies})


def about(request):
    return HttpResponse('<h1> Welcome to About page. </h1>')


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'detail.html', {'movie': movie})
