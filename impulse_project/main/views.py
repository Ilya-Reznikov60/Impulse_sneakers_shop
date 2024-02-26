from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    '''
    Index function
    '''
    context = {
        'title': 'Impulse - Главная'
    }

    return render(request, 'index.html', context)


def about(request):
    '''
    about function
    '''
    context = {
        'title': 'Impulse - О нас',
        'is_about_page': True,
    }

    return render(request, 'about.html', context)
