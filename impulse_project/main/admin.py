from django.contrib import admin

from main.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'content', 'image', 'published_date'
    )
