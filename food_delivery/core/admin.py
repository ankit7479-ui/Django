from django.contrib import admin
from .models import *

admin.site.register(Restaurant)
admin.site.register(FoodItem)
admin.site.register(Cart)
admin.site.register(Order)

