from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404;
from django.urls import reverse
from django.core import serializers;
from .forms import ProductForm
from .models import Product

def show_home(request):
    products = Product.objects.all() 
    return render(request, 'home.html', {'products': products})

def create_product(request):

    form = ProductForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('home'))

    return render(request, 'create-product.html', {'form': form})

def show_product(request):

    if request.method != 'GET':
        raise Http404
    
    format = request.GET.get('format', 'json')

    if format not in ['json', 'xml']:
        raise Http404
    
    type = ('application/json' if format == 'json' else 'application/xml') 

    data = Product.objects.all()
    return HttpResponse(serializers.serialize(format, data), content_type = type)

def show_product_by_id(request, id):

    if request.method != 'GET':
        raise Http404
    
    format = request.GET.get('format', 'json')

    if format not in ['json', 'xml']:
        raise Http404
    
    type = ('application/json' if format == 'json' else 'application/xml') 

    data = Product.objects.filter(pk = id)
    return HttpResponse(serializers.serialize(format, data), content_type = type)

def button_click(request):

    if request.method == 'POST':
        data = request.POST

        value = data.get('source')

        if value == 'clear':
            Product.objects.all().delete()

        return HttpResponseRedirect(reverse('home'))

    else:
        raise Http404
