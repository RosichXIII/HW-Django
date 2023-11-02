from django import forms
from .models import Product, ProductImg

class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=100)
    product_description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Описание продукта"}))
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = forms.IntegerField()
    # product_acceptance_date = forms.DateTimeField(auto_now_add=True)
    product_img = forms.ImageField(required = False)
    
class SelectProductById(forms.Form):
    id_product = forms.IntegerField()

class SelectProductByCustomerBydays(forms.Form):
    customer_id = forms.IntegerField()
    days = forms.IntegerField()