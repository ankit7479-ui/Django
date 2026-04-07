from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Get all restaurants
@api_view(['GET'])
def restaurants(request):
    data = Restaurant.objects.all()
    serializer = RestaurantSerializer(data, many=True)
    return Response(serializer.data)


# Get food items
@api_view(['GET'])
def food_items(request):
    data = FoodItem.objects.all()
    serializer = FoodItemSerializer(data, many=True)
    return Response(serializer.data)


# Add to cart
@api_view(['POST'])
def add_to_cart(request):
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Added to cart"})
    return Response(serializer.errors)


# Place order
@api_view(['POST'])
def place_order(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)

    total = sum([item.item.price * item.quantity for item in cart_items])

    order = Order.objects.create(user=user, total_price=total)
    for c in cart_items:
        order.items.add(c.item)

    cart_items.delete()

    return Response({"message": "Order placed successfully"})