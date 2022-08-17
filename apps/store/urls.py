from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='store_index'),
    path('product/<int:product_id>', views.product_details, name='store_product_details'),
]
