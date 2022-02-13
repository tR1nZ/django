from django.shortcuts import render

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
        'pics': [
            {'photo': '/static/img/controll.jpg'},
            {'photo': '/static/img/controll1.jpg'},
            {'photo': '/static/img/controll2.jpg'},
        ],
        'products':[
            {'pic': '/static/img/product-11.jpg'},
            {'pic': '/static/img/product-21.jpg'},
            {'pic': '/static/img/product-31.jpg'},
        ]

    }
    return render(request, 'products/products.html', сontext_products)
