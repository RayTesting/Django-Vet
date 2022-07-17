from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='home_index')
]
