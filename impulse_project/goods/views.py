from django.shortcuts import render

from goods.models import Product, Specification


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


def product(request, product_slug):
    '''
    product function
    '''

    product = Product.objects.get(slug=product_slug)
    specifications = Specification.objects.filter(
        products_with_specifications=product
    )

    context = {
        'title': 'Impulse - продукт',
        'is_product_page': True,
        'product': product,
        'specifications': specifications
    }

    return render(request, 'goods/product.html', context=context)
