from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('information/', views.info, name='info'),
    path('contacts/', views.contact, name='contact'),
    path('questions/', views.questions, name='questions'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy')
]
