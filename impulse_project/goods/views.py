from django.shortcuts import render, get_object_or_404

from goods.models import Product, Specification, Category


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


def catalog_by_category(request, category_slug):
    if category_slug == 'all':
        products = Product.objects.all()
        category = None
    else:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    return render(
        request, 'goods/catalog.html',
        {'goods': products, 'category': category}
    )
