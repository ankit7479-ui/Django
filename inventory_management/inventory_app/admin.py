from django.contrib import admin
from .models import Category, Product, Purchase, Consumption

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'category', 'current_stock', 'minimum_stock', 'unit_price', 'stock_value']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'sku']
    
@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'unit_price', 'total_amount', 'purchase_date', 'supplier']
    list_filter = ['purchase_date', 'product']
    search_fields = ['product__name', 'supplier', 'invoice_number']

@admin.register(Consumption)
class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'consumption_date', 'reason']
    list_filter = ['consumption_date', 'product']
    search_fields = ['product__name', 'reason']
