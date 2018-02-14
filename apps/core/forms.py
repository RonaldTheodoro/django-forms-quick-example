from django import forms


class OrderForm(forms.Form):
    person_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    product_name = forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)
