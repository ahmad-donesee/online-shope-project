from django import forms
from .models import Coupons

class  CouponForm(forms.Form):
    code=forms.CharField()