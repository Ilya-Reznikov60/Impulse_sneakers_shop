from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    '''
    Index function
    '''
    return render(request, 'index.html',)


def about(request):
    '''
    about function
    '''
    return HttpResponse('About Page')
