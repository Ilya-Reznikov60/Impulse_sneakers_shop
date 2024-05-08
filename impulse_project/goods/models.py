import random
import string

from django.db import models
from django.utils import timezone


class Size(models.Model):
    '''
    Модель Размеров
    '''
    name = models.CharField(
        max_length=10,
        verbose_name='Наименование размера'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name


class Specification(models.Model):
    '''
    Модель Характеристик
    '''
    name = models.CharField(
        max_length=150,
        verbose_name='Название характеристики'
    )
    gender = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Пол для продукта'
    )
    color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Цвет продукта'
    )
    country = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Страна производства'
    )
    composition = models.TextField(
        blank=True,
        null=True,
        verbose_name='Состав продукта'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.name


class Category(models.Model):
    '''
    Модель Категорий
    '''
    name = models.CharField(
        max_length=150, unique=True, verbose_name='Название категории'
    )
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    '''
    Модель Продукта
    '''
    name = models.CharField(
        max_length=200, unique=True, verbose_name='Название продукта'
    )
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(
        blank=True, null=True, verbose_name='Описание продукта'
    )
    price = models.IntegerField(
        default=0,
        verbose_name='Цена'
    )
    discount = models.DecimalField(
        default=0.00,
        max_digits=7,
        decimal_places=2,
        verbose_name='Скидка в %'
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество'
    )
    avaliable = models.BooleanField(
        default=True,
        verbose_name='Наличие'
    )
    category = models.ForeignKey(
        to=Category,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Выберите категорию'
    )
    specifications = models.ForeignKey(
        Specification,
        related_name='products_with_specifications',
        on_delete=models.CASCADE,
        verbose_name='Выберите характеристики'
    )
    is_new = models.BooleanField(
        default=False,
        verbose_name='Новый продукт'
    )
    sizes = models.ManyToManyField(
        'Size',
        related_name='products_sizes',
        verbose_name='Размеры'
    )
    related_product = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата и время добавления продукта'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        discount_amount = self.price * (self.discount / 100)
        discounted_price = self.price - discount_amount
        return discounted_price


class ProductImage(models.Model):
    '''
    Модель Изображения
    '''
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    image = models.ImageField(
        upload_to='goods_images',
        blank=True, null=True,
        verbose_name='Изображение'
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
