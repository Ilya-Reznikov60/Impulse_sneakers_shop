from django.shortcuts import render

from goods.models import Product


def catalog(request):
    '''
    catalog function
    '''
    goods = Product.objects.all()

    context = {
        'title': 'Impulse - Каталог',
        'is_catalog_page': True,
        'goods': goods,
    }

    return render(request, 'goods/catalog.html', context)


def product(request):
    '''
    product function
    '''
    context = {
        'title': 'Impulse - продукт',
        'is_product_page': True,
    }

    return render(request, 'goods/product.html', context)
