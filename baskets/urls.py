
from django.urls import re_path

import baskets.views as baskets

app_name = 'baskets'

urlpatterns = [
    re_path(r'^basket-add/<int:product_id>/$', baskets.basket_add, name='basket_add'),
    re_path(r'^basket-remove/<int:id>/$', baskets.basket_remove, name='basket_remove'),
    re_path(r'^basket-edit/<int:id>/<int:quantity>/$', baskets.basket_edit, name='basket_edit'),
]