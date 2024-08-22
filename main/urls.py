from django.urls import path, reverse
from django.http import HttpResponseRedirect;
from .views import *;

urlpatterns = [
    path('', lambda request: HttpResponseRedirect(reverse('home')), name='home-generic'),
    path('home', show_home, name='home'),
    path('create-product', create_product, name='create-product'),
    path('button-click', button_click, name='button-click'),
]