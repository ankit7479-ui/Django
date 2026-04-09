from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    sku = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=50, default='pcs')  # kg, liter, pcs, etc.
    current_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    minimum_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def stock_value(self):
        return self.current_stock * self.unit_price

    @property
    def is_low_stock(self):
        return self.current_stock <= self.minimum_stock

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(default=timezone.now)
    supplier = models.CharField(max_length=200, blank=True, null=True)
    invoice_number = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.quantity * self.unit_price
        super().save(*args, **kwargs)
        # Update product stock
        self.product.current_stock += self.quantity
        self.product.save()

    def __str__(self):
        return f"{self.product.name} - {self.quantity} {self.product.unit}"

class Consumption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='consumptions')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    consumption_date = models.DateTimeField(default=timezone.now)
    reason = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update product stock
        self.product.current_stock -= self.quantity
        self.product.save()

    def __str__(self):
        return f"{self.product.name} - {self.quantity} {self.product.unit} consumed"
