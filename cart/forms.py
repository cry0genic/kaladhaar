from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range (1,21)] # change as per req

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    overrride = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    