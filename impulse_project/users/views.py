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
        'title': 'Impulse - Мой профиль',
        'profile_header': 'Мой профиль'
    }
    return render(request, 'users/profile.html', context)


def my_orders(request):
    '''
    my_orders function.
    '''
    ...


def logout(request):
    '''
    logout function.
    '''
    ...
