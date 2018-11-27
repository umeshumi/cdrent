from django import forms
from .models import Product, Rent


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['Name', 'Rent_Price', 'Image']

class RentForm(forms.ModelForm):
	class Meta:
		model = Rent
		fields = ['days']