from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input100", "placeholder": "Username"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "input100", "placeholder": "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input100", "placeholder": "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input100", "placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LogInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input100", "placeholder": "Username or Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input100", "placeholder": "Password"}))
