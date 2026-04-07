from django.shortcuts import render
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Expense

@api_view(['GET'])
def monthly_summary(request):
    data = Expense.objects.filter(user=request.user) \
        .values('category') \
        .annotate(total=Sum('amount'))

    return Response(data)
