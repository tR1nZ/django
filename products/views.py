from django.shortcuts import render
from products.models import Product, ProductCategory

def index(request):
    context_index = {
        'title': 'Магазин', 
        'products': [
            {'name': 'Отличный стул', 'description': 'Расположитесь комфортно.', 'pic': '/static/img/product-1.jpg'},
            {'name': 'Стул повышенного качества', 'description': 'Не оторваться.', 'pic': 'static/img/product-2.jpg'}
        ]
    }
    return render(request, 'products/index.html', context_index)

def products(request):
    сontext_products = {
        'title': 'Каталог', 
        'pics': Product.objects.all,
        'products':[
            {'pic': '/static/img/product-11.jpg'},
            {'pic': '/static/img/product-21.jpg'},
            {'pic': '/static/img/product-31.jpg'},
        ]

    }
    return render(request, 'products/products.html', сontext_products)
