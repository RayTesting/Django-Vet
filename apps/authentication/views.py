from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, AuthForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login_method(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)

    return user


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


def signup(request):
    form = SignUpForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            user_form = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_index')
            else:
                msg = "ERROR AL AUTENTICAR"

        else:
            msg = 'Error'
    
    context = {
        "form": form,
        "msg": msg,
    }

    return render(request,'authentication/signup.html',context)