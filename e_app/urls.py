from django.urls import path
from .views import *

urlpatterns = [
    path('',home ,name='home'),
    path('contact',contactPage ,name='contact'),
    path('signup',signupPage ,name='signup'),
    path('signin',signinPage ,name='signin'),
    path('signout',signout ,name='signout'),
    path('menProducts',menProducts ,name='menProducts'),
    path('womenProducts',womenProducts ,name='womenProducts'),
    path('childProducts',childProducts ,name='childProducts'),
    path('accessories',accessoryProducts ,name='accessories'),
    path('toys',toyProducts ,name='toys'),
    path('product/<str:id>',productDetails ,name='product'),
    path('cart/',cartPage ,name='cart'),
    path('addtocart/<str:id>',addToCart ,name='addtocart'),
    path('removeFromCart/<uuid:product_id>/', removeFromCart, name='removeFromCart'),
    path('increaseCartItem/<uuid:product_id>/', increase_cart_item, name='increaseCartItem'),
    path('decreaseCartItem/<uuid:product_id>/', decrease_cart_item, name='decreaseCartItem'),
    path('fetch-cart-count/', fetch_cart_count, name='fetch-cart-count'),
]
