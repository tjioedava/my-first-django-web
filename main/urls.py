from django.urls import path
from django.shortcuts import redirect
from .views import *;

urlpatterns = [
    path('', lambda request: redirect('home'), name='home-generic'),
    path('home/', show_home, name='home'),
    path('create-product/', create_product, name='create-product'),
    path('button-click/', button_click, name='button-click'),
    path('show-product/', show_product, name='show-product'),
    path('show-product/<int:id>/', show_product_by_id, name='show-product-by-id'),
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
]