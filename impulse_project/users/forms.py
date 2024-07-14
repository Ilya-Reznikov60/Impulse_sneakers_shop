from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

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


class ProfileForm(UserChangeForm):
    '''
    Profile Form.
    '''

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField(required=False)
    username = forms.EmailField()
    gender = forms.CharField()
    date_of_birth = forms.CharField(required=False)
    city = forms.CharField(required=False)
    address = forms.CharField(required=False)
    postal_code = forms.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'image',
            'first_name',
            'last_name',
            'phone_number',
            'username',
            'gender',
            'date_of_birth',
            'city',
            'address',
            'postal_code'
        )
