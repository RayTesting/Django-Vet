from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.ProductsList.as_view(), name='store_index')
]
