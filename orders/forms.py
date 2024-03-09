from django import forms
from .models import Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


        
class OrderForm(forms.ModelForm):
    email=forms.EmailField(max_length=40)
    class Meta:
        model=Order
        fields=['first_name','last_name','address','phone','email','postal_code','city']

