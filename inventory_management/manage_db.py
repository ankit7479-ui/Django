# manage_db.py
import os
import django
import sqlite3
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_system.settings')
django.setup()

from inventory_app.models import Product, Category, Purchase, Consumption

class DatabaseManager:
    def __init__(self):
        self.db_path = 'db.sqlite3'
    
    def backup_database(self, backup_name=None):
        """Backup SQLite database"""
        if not backup_name:
            backup_name = f"db_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sqlite3"
        
        conn = sqlite3.connect(self.db_path)
        backup_conn = sqlite3.connect(backup_name)
        
        with backup_conn:
            conn.backup(backup_conn)
        
        conn.close()
        backup_conn.close()
        print(f"✅ Database backed up to: {backup_name}")
        return backup_name
    
    def clear_all_data(self):
        """Clear all data from tables (except users)"""
        confirm = input("⚠️  This will delete ALL data! Type 'YES' to confirm: ")
        if confirm == 'YES':
            Product.objects.all().delete()
            Category.objects.all().delete()
            Purchase.objects.all().delete()
            Consumption.objects.all().delete()
            print("✅ All data cleared!")
        else:
            print("❌ Operation cancelled")
    
    def run_custom_query(self, query):
        """Run custom SQL query"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(query)
            
            if query.strip().upper().startswith('SELECT'):
                results = cursor.fetchall()
                for row in results:
                    print(row)
            else:
                conn.commit()
                print(f"✅ Query executed successfully! {cursor.rowcount} rows affected.")
            
            conn.close()
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def show_table_schema(self, table_name):
        """Show schema of specific table"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        
        print(f"\n📋 Schema for table: {table_name}")
        print("-" * 50)
        for col in columns:
            print(f"  {col[1]} : {col[2]} (Default: {col[4]})")
        conn.close()

# Usage examples
if __name__ == "__main__":
    db = DatabaseManager()
    
    # Backup database
    db.backup_database()
    
    # Show schema
    db.show_table_schema('inventory_app_product')
    
    # Run custom query
    db.run_custom_query("SELECT * FROM inventory_app_product LIMIT 5;")