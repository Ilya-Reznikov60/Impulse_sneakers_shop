# Generated by Django 3.2.16 on 2024-03-10 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название категории')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название характеристики')),
                ('gender', models.CharField(blank=True, max_length=15, null=True, verbose_name='Пол для продукта')),
                ('color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Цвет продукта')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Страна производства')),
                ('composition', models.TextField(blank=True, null=True, verbose_name='Состав продукта')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название продукта')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание продукта')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Скидка в %')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('avaliable', models.BooleanField(default=True, verbose_name='Наличие')),
                ('is_new', models.BooleanField(default=False, verbose_name='Новый продукт')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='goods.category', verbose_name='Выберите категорию')),
                ('specifications', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_with_specifications', to='goods.specification', verbose_name='Выберите характеристики')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('name',),
            },
        ),
    ]
