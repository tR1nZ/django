from django.urls import re_path
import products.views as products

app_name = 'products'

urlpatterns = [
    re_path(r'^$', products.products, name='index'),
    re_path(r'^category/(?P<pk>\d+)/$', products.products, name='category'),
    re_path(r'^/page/(?P<page>\d+)/$', products.products, name='page'),
]