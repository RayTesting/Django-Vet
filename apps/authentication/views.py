from hashlib import new
from sys import prefix
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from ..home.models import Customer
from .forms import CustomerForm, LoginForm, AuthForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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
                next = request.GET.get('next')
                if next: 
                    return redirect(next)
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
    signup_form = SignUpForm(request.POST or None, prefix='signup')
    customer_form = CustomerForm(request.POST or None, prefix='customer')
    msg = None

    if request.method == "POST":
        if signup_form.is_valid() and customer_form.is_valid():

            user_form = signup_form.save()
            new_customer = customer_form.save(commit=False)
            
            username = signup_form.cleaned_data.get('username')
            email = signup_form.cleaned_data.get('email')
            password = signup_form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                new_customer.user = user
                new_customer.save()
                return redirect('home_index')
            else:
                msg = "ERROR AL AUTENTICAR"

        else:
            msg = 'Error'
    
    context = {
        "signup_form": signup_form,
        "customer_form": customer_form,
        "msg": msg,
    }

    return render(request,'authentication/signup.html',context)

@login_required(login_url='auth_login')
def account_details(request):
    account = Customer.objects.get(user=request.user)
    context = {
        "account": account
    }
    return render(request,'authentication/account_details.html',context)
