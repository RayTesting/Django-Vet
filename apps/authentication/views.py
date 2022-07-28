from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, AuthForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login_view(request):
    msg = None
    form = AuthForm(data=request.POST or None)

    if request.user.is_authenticated:
        return redirect('home_index')

    if request.method == "POST":
        if form.is_valid():
            print('is valid')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_index')
            else:
                msg = "USERNAME OR PASSWORD INCORRECT"
        else:
            print('is not valid')

    return render(request, 'authentication/login.html',{"msg":msg, "form":form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('auth_login')