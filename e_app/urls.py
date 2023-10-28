from django.urls import path
from .views import *

urlpatterns = [
    path('',home ,name='home'),
    path('signup',signupPage ,name='signup'),
    path('signin',signinPage ,name='signin'),
    path('signout',signout ,name='signout'),
    path('productList',productList ,name='productList'),
    path('product/<str:id>',productDetails ,name='product'),
    path('cart/',cartPage ,name='cart'),
    path('addtocart/<str:id>',addToCart ,name='addtocart'),
    path('removeFromCart/<uuid:product_id>/', removeFromCart, name='removeFromCart'),
    path('increase-cart-item/<uuid:product_id>/', increase_cart_item, name='increase-cart-item'),
    path('decrease-cart-item/<uuid:product_id>/', decrease_cart_item, name='decrease-cart-item'),
    path('fetch-cart-count/', fetch_cart_count, name='fetch-cart-count'),
]
