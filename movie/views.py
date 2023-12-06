from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    search_term = request.GET.get('searchMovie')
    return render(request, 'home.html', {'searchTerm': search_term})


def about(request):
    return HttpResponse('<h1> Welcome to About page. </h1>')


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})