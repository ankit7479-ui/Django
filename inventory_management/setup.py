import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_system.settings')
django.setup()

from django.contrib.auth.models import User
from inventory_app.models import Category, Product

def setup_demo_data():
    # Create superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Admin user created: admin/admin123")
    
    # Create manager user
    if not User.objects.filter(username='manager').exists():
        User.objects.create_user('manager', 'manager@example.com', 'manager123')
        print("Manager user created: manager/manager123")
    
    # Create categories
    categories = ['Beverages', 'Food Ingredients', 'Cleaning Supplies', 'Packaging']
    for cat_name in categories:
        Category.objects.get_or_create(name=cat_name)
    
    # Create sample products
    products_data = [
        {'name': 'Coffee Beans', 'sku': 'BEV001', 'category': 'Beverages', 'current_stock': 50, 'minimum_stock': 10, 'unit_price': 15.99},
        {'name': 'Sugar', 'sku': 'ING001', 'category': 'Food Ingredients', 'current_stock': 100, 'minimum_stock': 20, 'unit_price': 0.99},
        {'name': 'Milk', 'sku': 'BEV002', 'category': 'Beverages', 'current_stock': 30, 'minimum_stock': 15, 'unit_price': 2.49},
        {'name': 'Cleaning Spray', 'sku': 'CLN001', 'category': 'Cleaning Supplies', 'current_stock': 5, 'minimum_stock': 10, 'unit_price': 4.99},
    ]
    
    for product_data in products_data:
        category = Category.objects.get(name=product_data['category'])
        Product.objects.get_or_create(
            name=product_data['name'],
            defaults={
                'sku': product_data['sku'],
                'category': category,
                'current_stock': product_data['current_stock'],
                'minimum_stock': product_data['minimum_stock'],
                'unit_price': product_data['unit_price'],
                'unit': 'kg' if product_data['name'] == 'Sugar' else 'pcs'
            }
        )
    
    print("Demo data setup complete!")

if __name__ == "__main__":
    setup_demo_data()