from django import forms
from .models import Product, Purchase, Consumption, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'sku', 'unit', 'current_stock', 'minimum_stock', 'unit_price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SKU Number'}),
            'unit': forms.Select(attrs={'class': 'form-control'}, choices=[('pcs', 'Pieces'), ('kg', 'Kilograms'), ('liter', 'Liters'), ('box', 'Box')]),
            'current_stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Current Stock'}),
            'minimum_stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minimum Stock Level'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unit Price'}),
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product', 'quantity', 'unit_price', 'supplier', 'invoice_number']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unit Price'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supplier Name'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Invoice Number'}),
        }

class ConsumptionForm(forms.ModelForm):
    class Meta:
        model = Consumption
        fields = ['product', 'quantity', 'reason']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity Consumed'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Reason for consumption'}),
        }