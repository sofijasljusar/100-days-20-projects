from django import forms
from .models import Cafe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'img_url': forms.URLInput(attrs={'class': 'form-control'}),
            'coffee_price': forms.TextInput(attrs={'class': 'form-control'}),
            'seats': forms.TextInput(attrs={'class': 'form-control'}),
            'has_wifi': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_sockets': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_toilet': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_take_calls': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
