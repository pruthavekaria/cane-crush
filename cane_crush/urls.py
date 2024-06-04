from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products', products, name='products'),
    path('product/<slug:slug>/', product_view, name='product'),
    path('cart', view_cart, name='cart'),
]
