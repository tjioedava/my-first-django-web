from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect;
from django.urls import reverse
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
