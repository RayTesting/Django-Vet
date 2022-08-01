from itertools import product
from django.http import HttpResponse
from django.shortcuts import render
from .models import SiteSettings
from apps.store.models import Product, ProductCategory

# Create your views here.
def index(request):
    settings = SiteSettings.objects.first()
    product_categories = ProductCategory.objects.all()
    recomended = Product.objects.all()[:10:-1]
    context = {
        "settings": settings,
        "product_categories": product_categories,
        "recomended": recomended
    }
    return render(request, 'home/index.html',context)