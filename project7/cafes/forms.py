from django import forms
from .models import Cafe


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
