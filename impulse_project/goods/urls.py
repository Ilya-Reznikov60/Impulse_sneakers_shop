from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('new-items/', views.new_items, name='new_items'),
    path('sale/', views.sale_items, name='sale'),
    path('<slug:category_slug>/', views.catalog_by_category,
         name='catalog_by_category'),
    path('', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]
