from django.contrib.auth import login, logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import CreateForm


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
