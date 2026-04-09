# inspect_db.py
import os
import django
import sqlite3

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_system.settings')
django.setup()

from django.db import connection
from inventory_app.models import Product, Category, Purchase, Consumption
from django.contrib.auth.models import User

def inspect_database():
    print("=" * 60)
    print("DATABASE INSPECTION REPORT")
    print("=" * 60)
    
    # 1. Show all tables
    print("\n📋 TABLES IN DATABASE:")
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        tables = cursor.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
    
    # 2. Show record counts
    print("\n📊 RECORD COUNTS:")
    print(f"  Categories: {Category.objects.count()}")
    print(f"  Products: {Product.objects.count()}")
    print(f"  Purchases: {Purchase.objects.count()}")
    print(f"  Consumptions: {Consumption.objects.count()}")
    print(f"  Users: {User.objects.count()}")
    
    # 3. Show database file size
    db_path = os.path.join(os.getcwd(), 'db.sqlite3')
    if os.path.exists(db_path):
        size = os.path.getsize(db_path) / (1024 * 1024)  # Convert to MB
        print(f"\n💾 DATABASE SIZE: {size:.2f} MB")
    
    # 4. Show schema of Product table
    print("\n🔧 PRODUCT TABLE SCHEMA:")
    with connection.cursor() as cursor:
        cursor.execute("PRAGMA table_info(inventory_app_product);")
        columns = cursor.fetchall()
        for col in columns:
            print(f"  - {col[1]}: {col[2]} (nullable: {not col[3]})")
    
    # 5. Show sample data
    print("\n📦 SAMPLE PRODUCTS (first 5):")
    products = Product.objects.all()[:5]
    for product in products:
        print(f"  • {product.name} - Stock: {product.current_stock} - Price: ${product.unit_price}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    inspect_database()
    