from django.urls import path, reverse
from django.http import HttpResponseRedirect;
from .views import show_home;

urlpatterns = [
    path('', lambda request: HttpResponseRedirect(reverse('home')), name='home-generic'),
    path('home', show_home, name='home'),
]