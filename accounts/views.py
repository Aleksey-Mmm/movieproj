from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import CreateForm, LoginForm


def signup_account(request):
    if request.method == 'GET':
        return render(request, 'signup_account.html', {'form': CreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup_account.html',
                              {'form': CreateForm,
                               'error_message': 'Имя уже занято! Выберите другое.'})
        else:
            return render(request, 'signup_account.html', {'form': CreateForm,
                                                           'error_message': 'Passwords do not match!'})


def logout_account(request):
    logout(request)
    return redirect('home')


def login_account(request):
    if request.method == 'GET':
        return render(request, 'login_account.html', {'form': LoginForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login_account.html', {'form': LoginForm,
                                                          'error_message': 'Неверный логин или пароль!'})
        else:
            login(request, user)
            return redirect('home')
    