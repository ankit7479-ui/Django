from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.restaurants),
    path('foods/', views.food_items),
    path('cart/', views.add_to_cart),
    path('order/', views.place_order),
]