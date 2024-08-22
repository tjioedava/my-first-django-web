from django.shortcuts import render
from django.http import HttpResponse;

def show_home(request):
    return render(request, 'home.html', dict())
