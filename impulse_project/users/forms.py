from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    '''
    User Form.
    '''

    username = forms.EmailField()
    password = forms.CharField()

    '''username = forms.EmailField(widget=forms.EmailInput(attrs={
        'autofocus': True,
        'class': 'custom-email-field',
        'placeholder': 'Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'autofocus': True,
        'class': 'custom-password-field',
        'placeholder': 'Пароль'
    }))'''

    class Meta:
        model = User
        fields = ['username', 'password']
