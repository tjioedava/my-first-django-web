from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.shortcuts import redirect;
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime
from .forms import ProductForm
from .models import Product

@login_required(login_url='/login/')
def show_home(request):
    products = Product.objects.all() 
    context = {
        'products': products,
        'last_login': request.COOKIES.get('last_login', '-'),
    }
    return render(request, 'home.html', context)

@login_required(login_url='/login/')
def create_product(request):

    form = ProductForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'create-product.html', {'form': form})

@login_required(login_url='/login/')
def show_product(request):

    if request.method != 'GET':
        raise Http404
    
    format = request.GET.get('format', 'json')

    if format not in ['json', 'xml']:
        raise Http404
    
    type = ('application/json' if format == 'json' else 'application/xml') 

    data = Product.objects.all()
    return HttpResponse(serializers.serialize(format, data), content_type = type)

@login_required(login_url='/login/')
def show_product_by_id(request, id):

    if request.method != 'GET':
        raise Http404
    
    format = request.GET.get('format', 'json')

    if format not in ['json', 'xml']:
        raise Http404
    
    type = ('application/json' if format == 'json' else 'application/xml') 

    data = Product.objects.filter(pk = id)
    return HttpResponse(serializers.serialize(format, data), content_type = type)

def register(request):

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.info(request, 'The form is invalid')
        
    return render(request, 'register.html', {'form': form})

def log_in(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(request.GET.get('next') or reverse('home'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Login failed')
        
    return render(request, 'login.html', dict())

def button_click(request):

    if request.method != 'POST':
        raise Http404
    data = request.POST

    action = data.get('source')

    if action == 'clear':
        Product.objects.all().delete()

    if action == 'logout':
        logout(request)
        response = HttpResponseRedirect(reverse('login'))
        response.delete_cookie('last_login')
        return response

    return redirect('home')
