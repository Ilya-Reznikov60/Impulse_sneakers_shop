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


def product(request, product_id):
    '''
    product function
    '''

    product = Product.objects.get(id=product_id)
    specifications = Specification.objects.filter(products_with_specifications=product_id)

    context = {
        'title': 'Impulse - продукт',
        'is_product_page': True,
        'product': product,
        'specifications': specifications
    }

    return render(request, 'goods/product.html', context=context)
