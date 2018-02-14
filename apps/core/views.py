from django.shortcuts import render
from . import forms, models

def index(request):
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            models.Person.objects.create(
                person_name=form.cleaned_data.get('person_name'),
                phone=form.cleaned_data.get('phone')
            )

            models.Product.objects.create(
                product_name=form.cleaned_data.get('product_name'),
                category=form.cleaned_data.get('category')
            )
    else:
        form = forms.OrderForm()
    return render(request, 'index.html', {'form': form})