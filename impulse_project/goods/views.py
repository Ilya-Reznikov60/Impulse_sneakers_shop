from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from goods.models import Product, Specification, Category


NUMBER_OF_GOODS = 3


def get_page(request, goods_list):
    paginator = Paginator(goods_list, NUMBER_OF_GOODS)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def sort_products(products, sort_by):
    if sort_by == 'price-asc':
        return products.order_by('price')
    elif sort_by == 'price-desc':
        return products.order_by('-price')
    else:
        return products


def catalog(request):
    '''
    catalog function
    '''
    goods = Product.objects.all()

    if request.method == 'GET' and 'sort_by' in request.GET:
        sort_by = request.GET['sort_by']
        goods = sort_products(goods, sort_by)

    page_obj = get_page(request, goods)

    context = {
        'title': 'Impulse - Каталог',
        'is_catalog_page': True,
        'goods': page_obj,
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

    if request.method == 'GET' and 'sort_by' in request.GET:
        sort_by = request.GET['sort_by']
        products = sort_products(products, sort_by)

    page_obj = get_page(request, products)

    return render(
        request, 'goods/catalog.html',
        {'goods': page_obj, 'category': category}
    )


def new_items(request):
    '''
    new products function
    '''
    new_goods = Product.objects.filter(is_new=True)

    if request.method == 'GET' and 'sort_by' in request.GET:
        sort_by = request.GET['sort_by']
        new_goods = sort_products(new_goods, sort_by)

    page_obj = get_page(request, new_goods)

    context = {
        'title': 'Impulse - Новинки',
        'is_new_items_page': True,
        'goods': page_obj,
    }

    return render(request, 'goods/new_items.html', context)


def sale_items(request):
    '''
    sale products function
    '''
    sale_goods = Product.objects.filter(discount__gt=0)

    if request.method == 'GET' and 'sort_by' in request.GET:
        sort_by = request.GET['sort_by']
        sale_goods = sort_products(sale_goods, sort_by)

    page_obj = get_page(request, sale_goods)

    context = {
        'title': 'Impulse - Распродажа',
        'is_sale_items_page': True,
        'goods': page_obj,
    }

    return render(request, 'goods/sale.html', context)
