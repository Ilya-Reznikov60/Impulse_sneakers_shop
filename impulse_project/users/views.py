from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import (
    UserLoginForm, UserRegistrationForm, ProfileForm
)


def login(request):
    '''
    login function.
    '''
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Impulse - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    '''
    registration function.
    '''
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Impulse - Регистрация',
        'form': form,
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    '''
    profile function.
    '''
    if request.method == 'POST':
        form = ProfileForm(
            data=request.POST,
            instance=request.user,
            files=request.FILES
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Impulse - Мой профиль',
        'profile_header': 'Мой профиль',
        'form': form
    }
    return render(request, 'users/profile.html', context)


def my_orders(request):
    '''
    my_orders function.
    '''
    ...


@login_required
def logout(request):
    '''
    logout function.
    '''
    auth.logout(request)
    return redirect(reverse('main:index'))
