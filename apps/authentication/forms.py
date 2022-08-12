from dataclasses import field, fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuario',
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"User",
                "class":"border border-slate-600"
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Contraseña",
                "class":"border border-slate-600"
            }
        )
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
           attrs={
                "placeholder":"User",
                "class":"border border-slate-600"
            } 
        )
    )

    email = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder":"Email",
                "class":"border border-slate-600"
            } 
        )
    )

    password1 = forms.CharField(
        label='Password1',
        required=True,
        widget=forms.PasswordInput(
           attrs={
                "placeholder":"Password",
                "class":"border border-slate-600"
            } 
        )
    )

    password2 = forms.CharField(
        label='Password2',
        required=True,
        widget=forms.PasswordInput(
           attrs={
                "placeholder":"Password",
                "class":"border border-red-600"
            } 
        )
    )

    class Meta:
        model= User
        fields = ('username','email','password1','password2')

class AuthForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario',
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"User",
                "class":"border border-slate-600"
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Contraseña",
                "class":"border border-slate-600"
            }
        )
    )

    class Meta:
        model = User
        # fields = '__all__' todos
        # fields = 'username' solo uno
        # fields = ('username', 'password') varios