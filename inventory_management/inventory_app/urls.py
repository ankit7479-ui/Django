from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('purchase-entry/', views.purchase_entry, name='purchase_entry'),
    path('stock-report/', views.stock_report, name='stock_report'),
    path('consumption-report/', views.consumption_report, name='consumption_report'),
    path('purchase-report/', views.purchase_report, name='purchase_report'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-category/', views.add_category, name='add_category'),
    path('daily-consumption/', views.daily_consumption, name='daily_consumption'),
]