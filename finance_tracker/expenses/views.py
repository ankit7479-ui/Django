from django.shortcuts import render
from rest_framework import viewsets
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.permissions import IsAuthenticated

from .models import Expense

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()   # ✅ ADD THIS
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)