from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'store/index.html',context)

class ProductsList(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'
    

    

