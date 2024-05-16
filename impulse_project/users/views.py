from django.shortcuts import render


def login(request):
    '''
    login function.
    '''
    context = {
        'title': 'Impulse - Авторизация'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    '''
    registration function.
    '''
    context = {
        'title': 'Impulse - Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    '''
    profile function.
    '''
    context = {
        'title': 'Impulse - Мой профиль'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    '''
    logout function.
    '''
    ...
