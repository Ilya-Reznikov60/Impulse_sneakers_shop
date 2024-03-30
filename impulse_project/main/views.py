from django.http import HttpResponse
from django.shortcuts import render


from goods.models import Category, Product
from main.models import News


def index(request):
    '''
    Index function
    '''
    categories = Category.objects.all()
    goods = Product.objects.all()
    news = News.objects.all()
    context = {
        'title': 'Impulse - Главная',
        'categories': categories,
        'goods': goods,
        'news': news,
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


def info(request):
    '''
    information function
    '''
    context = {
        'title': 'Impulse - Доставка и оплата',
        'is_info_page': True,
    }

    return render(request, 'main/information.html', context)


def contact(request):
    '''
    contact function
    '''
    context = {
        'title': 'Impulse - Контакты',
        'is_contact_page': True,
    }

    return render(request, 'main/contacts.html', context)


def questions(request):
    '''
    questions function
    '''
    context = {
        'title': 'Impulse - Вопросы и ответы',
        'is_questions_page': True,
    }

    return render(request, 'main/questions.html', context)


def privacy_policy(request):
    '''
    privacy_policy function
    '''
    context = {
        'title': 'Impulse - Политика конфиденциальности',
        'is_privacy_page': True,
    }

    return render(request, 'main/privacy_policy.html', context)
