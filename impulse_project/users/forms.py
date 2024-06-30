from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    '''
    Login Form.
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


class UserRegistrationForm(UserCreationForm):
    '''
    Registration Form.
    '''

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        )
