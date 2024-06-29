from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
    Модель пользователя.
    '''
    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )
    image = models.ImageField(
        upload_to='users_managers',
        blank=True,
        null=True,
        verbose_name='Фото профиля'
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        verbose_name='Номер телефона'
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата рождения'
    )
    gender = models.CharField(
        max_length=10,
        blank=True,
        verbose_name='Пол'
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Город проживания'
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Адрес проживания'
    )
    postal_code = models.CharField(
        max_length=10,
        blank=True,
        verbose_name='Почтовый индекс'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
