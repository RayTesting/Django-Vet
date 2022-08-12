from . import views
from django.urls import include, path

urlpatterns = [
    path('login/', views.login_view, name='auth_login'),
    path('logout/', views.logout_view, name="auth_logout"),
    path('signup/', views.signup, name="auth_signup"),
]
