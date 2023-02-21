from django.urls import path

from webapp.views.base import index_view
from webapp.views.category import category_add_view
from webapp.views.product import detail_view, product_add_view

urlpatterns = [
    path('', index_view, name='index'),
    path('products', index_view, name='index'),
    path('products/add', product_add_view, name='product_add'),
    path('products/<int:pk>', detail_view, name='product_detail'),
    path('categories/add', category_add_view, name='category_add')
]
