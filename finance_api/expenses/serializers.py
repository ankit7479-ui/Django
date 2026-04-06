from rest_framework import serializers
from .models import Expense
from django.contrib.auth.models import User

class  ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
        
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']   # ✅ REQUIRED

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)