from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, Review
from django.shortcuts import get_object_or_404
from .forms import ReviewForm


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
    rewiews = Review.objects.filter(movie=movie)
    return render(request, 'detail.html', {'movie': movie, 'reviews': rewiews})


def create_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        return render(request, 'create_review.html', {
            'form': ReviewForm(), 'movie': movie})
    else:
        try:
            form = ReviewForm(request.POST)
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.movie = movie
            new_review.save()
            return redirect('detail', new_review.movie.id)
        except ValueError:
            return render(request, 'create_review.html', {
                'form': ReviewForm(), 'error': 'Получены некорректные данные.'})