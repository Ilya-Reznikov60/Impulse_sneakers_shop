from django.http import HttpResponse
from django.shortcuts import render


from goods.models import Category


def index(request):
    '''
    Index function
    '''
    categories = Category.objects.all()
    context = {
        'title': 'Impulse - Главная',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)


def about(request):
    '''
    about function
    '''
    context = {
        'title': 'Impulse - О нас',
        'is_about_page': True,
    }

    return render(request, 'main/about.html', context)
