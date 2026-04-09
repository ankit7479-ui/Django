from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count, Q, F
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Product, Purchase, Consumption, Category
from .forms import ProductForm, PurchaseForm, ConsumptionForm, CategoryForm
from .decorators import unauthenticated_user

@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    total_products = Product.objects.count()
    low_stock_items = Product.objects.filter(current_stock__lte=F('minimum_stock')).count()
    total_stock_value = Product.objects.aggregate(total=Sum(F('current_stock') * F('unit_price')))['total'] or 0
    
    # Recent purchases
    recent_purchases = Purchase.objects.select_related('product').order_by('-purchase_date')[:5]
    
    # Recent consumptions
    recent_consumptions = Consumption.objects.select_related('product').order_by('-consumption_date')[:5]
    
    # Low stock products
    low_stock_products = Product.objects.filter(current_stock__lte=F('minimum_stock'))[:10]
    
    context = {
        'total_products': total_products,
        'low_stock_items': low_stock_items,
        'total_stock_value': total_stock_value,
        'recent_purchases': recent_purchases,
        'recent_consumptions': recent_consumptions,
        'low_stock_products': low_stock_products,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def purchase_entry(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.created_by = request.user
            purchase.save()
            messages.success(request, 'Purchase recorded successfully!')
            return redirect('purchase_entry')
    else:
        form = PurchaseForm()
    
    purchases = Purchase.objects.select_related('product', 'created_by').order_by('-purchase_date')[:20]
    
    context = {
        'form': form,
        'purchases': purchases,
    }
    return render(request, 'purchase_entry.html', context)

@login_required(login_url='login')
def stock_report(request):
    products = Product.objects.select_related('category').all()
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
    
    # Search
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(sku__icontains=search_query)
        )
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query,
    }
    return render(request, 'stock_report.html', context)

@login_required(login_url='login')
def consumption_report(request):
    consumptions = Consumption.objects.select_related('product', 'created_by').order_by('-consumption_date')
    
    # Date filters
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    
    if date_from:
        consumptions = consumptions.filter(consumption_date__gte=date_from)
    if date_to:
        consumptions = consumptions.filter(consumption_date__lte=date_to)
    
    # Product filter
    product_id = request.GET.get('product')
    if product_id:
        consumptions = consumptions.filter(product_id=product_id)
    
    total_consumed = consumptions.aggregate(total=Sum('quantity'))['total'] or 0
    
    products = Product.objects.all()
    
    context = {
        'consumptions': consumptions,
        'products': products,
        'total_consumed': total_consumed,
        'date_from': date_from,
        'date_to': date_to,
    }
    return render(request, 'consumption_report.html', context)

@login_required(login_url='login')
def purchase_report(request):
    purchases = Purchase.objects.select_related('product', 'created_by').order_by('-purchase_date')
    
    # Date filters
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    
    if date_from:
        purchases = purchases.filter(purchase_date__gte=date_from)
    if date_to:
        purchases = purchases.filter(purchase_date__lte=date_to)
    
    # Product filter
    product_id = request.GET.get('product')
    if product_id:
        purchases = purchases.filter(product_id=product_id)
    
    total_purchases = purchases.aggregate(total=Sum('total_amount'))['total'] or 0
    
    products = Product.objects.all()
    
    context = {
        'purchases': purchases,
        'products': products,
        'total_purchases': total_purchases,
        'date_from': date_from,
        'date_to': date_to,
    }
    return render(request, 'purchase_report.html', context)

@login_required(login_url='login')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('stock_report')
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})

@login_required(login_url='login')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('stock_report')
    else:
        form = CategoryForm()
    
    return render(request, 'add_category.html', {'form': form})

def daily_consumption(request):
    return consumption_report(request)