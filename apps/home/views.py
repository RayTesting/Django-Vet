from django.http import HttpResponse
from django.shortcuts import render

from apps.store.models import ProductCategory, Product

from .models import SiteSettings

# Create your views here.
def index(request):
    settings = SiteSettings.objects.first()
    product_categories = ProductCategory.objects.all()
    recommended = Product.objects.all()[:10:-1]
    context = {
        "settings":settings,
        "product_categories": product_categories,
        "recommended": recommended,
    }


    return render(request, 'home/index.html',context)