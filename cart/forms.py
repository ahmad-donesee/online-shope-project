from django import forms

PRODUCT_QUANTITY_CHOICES= [(i,str(i)) for i in range(1,21)]


class Product_quantity_Form(forms.Form):
    quantity=forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
    overide=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)