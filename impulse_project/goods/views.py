from django.shortcuts import render


def catalog(request):
    '''
    catalog function
    '''
    context = {
        'title': 'Impulse - Каталог',
        'is_catalog_page': True,
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
