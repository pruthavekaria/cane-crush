from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('products', products, name='products'),
    path('product/<slug:slug>/', product_view, name='product'),
    path('cart', view_cart, name='cart'),
    path('contact_us', contact_us, name='contact_us'),
    path('delete_cart/<int:id>/', remove_item_from_cart, name='delete_cart'),
]
