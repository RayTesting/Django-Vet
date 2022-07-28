from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

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