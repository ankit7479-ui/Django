from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_view, name='create'),
    path('create_emp/', views.create_emp, name='create_emp'),

    # ✅ FIX HERE
    path('update/<int:id>/', views.update_view, name='update'),
    path('update_emp/<int:id>/', views.update_emp, name='update_emp'),
    path('delete/<int:id>/', views.delete, name='delete'),
]