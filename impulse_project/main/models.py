from django.db import models


class News(models.Model):
    '''
    News model
    '''
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок'
    )
    description = models.CharField(
        max_length=300,
        verbose_name='Короткое описание новости'
    )
    content = models.TextField(
        verbose_name='Текст новости'
    )
    image = models.ImageField(
        upload_to='news-images/',
        verbose_name='Картинка новости'
    )
    published_date = models.DateField(
        verbose_name='Дата публикации'
    )

    class Meta:
        ordering = ('-published_date',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
