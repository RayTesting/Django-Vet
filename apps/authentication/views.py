from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    msg = None

    if request.user.is_authenticated:
        return redirect('home_index')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_index')
        else:
            msg = "USERNAME OR PASSWORD INCORRECT"

    return render(request, 'authentication/login.html',{"msg":msg})