from . import views
from django.urls import include, path

urlpatterns = [
    path('login/', views.login_view, name='auth_login')
]
