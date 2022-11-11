from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from django.core.paginator import Paginator  
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    products = Product.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(products, 2)
    products = paginator.get_page(page)
    context = {
        "products": products
    }
    return render(request, 'store/index.html',context)

class ProductsList(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'

@login_required(login_url='/auth/login')
def product_details(request, product_id):

    try:
        product = Product.objects.get(id=product_id)

        context = {
            "product": product,
        }

        return render(request,'store/product_details.html', context)
    except Product.DoesNotExist:
        raise Http404('Product Not found')
    

