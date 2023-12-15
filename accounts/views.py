from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signup_account(request):
    return render(request, 'signup_account.html', {'form': UserCreationForm})
