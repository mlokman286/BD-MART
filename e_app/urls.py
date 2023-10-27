from django.urls import path

from .views import *


urlpatterns = [
    path('',home ,name='home'),
    path('/menProduct',menProduct ,name='menProduct'),
    path('product/<str:id>',productDetails ,name='product'),
]
