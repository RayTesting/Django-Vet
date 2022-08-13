from dataclasses import field, fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from ..home.models import Customer

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
        label='Password',
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
                "class":"border border-[#113E21] rounded w-full p-2"
            } 
        )
    )

    email = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder":"Email",
                "class":"border border-[#113E21] rounded w-full p-2"
            } 
        )
    )

    password1 = forms.CharField(
        label='Password1',
        required=True,
        widget=forms.PasswordInput(
           attrs={
                "placeholder":"Password",
                "class":"border border-[#113E21] rounded w-full p-2"
            } 
        )
    )

    password2 = forms.CharField(
        label='Password2',
        required=True,
        widget=forms.PasswordInput(
           attrs={
                "placeholder":"Password",
                "class":"border border-[#113E21] rounded w-full p-2"
            } 
        )
    )

    class Meta:
        model= User
        fields = ('username','email','password1','password2')

class CustomerForm(forms.ModelForm):

    name = forms.CharField(
        label='Name',
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class":"border border-[#113E21] rounded w-full p-2"
            }
        )
    )

    last_name = forms.CharField(
        label='Last name',
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
                "class":"border border-[#113E21] rounded w-full p-2"
            }
        )
    )

    birth = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "type":"date",
                "class":"border border-[#113E21] rounded w-full p-2"
            }
        )
    )

    class Meta:
        model = Customer
        fields = ('name','last_name','birth')

class AuthForm(AuthenticationForm):
    username = forms.CharField(
        label='User',
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Enter your username",
                "class":"border border-[#113E21] rounded w-full p-2"
            }
        )
    )

    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Enter your password",
                "class":"border border-[#113E21] rounded w-full p-2"
            }
        )
    )

    class Meta:
        model = User
        # fields = '__all__' todos
        # fields = 'username' solo uno
        # fields = ('username', 'password') varios