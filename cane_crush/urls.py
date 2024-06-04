from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('products', products, name='products'),
    path('product/<slug:slug>/', product_view, name='product'),
    path('cart', view_cart, name='cart'),
    path('contact_us', contact_us, name='contact_us'),
]
