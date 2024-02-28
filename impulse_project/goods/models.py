from django.db import models


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
    image = models.ImageField(
        upload_to='goods_images',
        blank=True, null=True,
        verbose_name='Изображение'
    )
    price = models.DecimalField(
        default=0.00,
        max_digits=7,
        decimal_places=2,
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

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'
