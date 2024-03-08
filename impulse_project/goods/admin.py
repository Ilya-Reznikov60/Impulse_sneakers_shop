from django.contrib import admin

from goods.models import Category, Product, Specification

# admin.site.register(Category)
# admin.site.register(Product)


@admin.register(Specification)
class Specification(admin.ModelAdmin):
    list_display = ('name', 'gender', 'color', 'country', 'composition')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
