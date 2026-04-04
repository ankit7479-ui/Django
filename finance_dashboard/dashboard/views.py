from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from finance.models import FinancialRecord
from users.permissions import IsAnalystOrAdmin

# Create your views here.
class DashboardSummaryView(APIView):
      permission_classes = [IsAnalystOrAdmin]
      def get(self, request):
        records = FinancialRecord.objects.all()

        income = records.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        expense = records.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

        return Response({
            "total_income": income,
            "total_expense": expense,
            "net_balance": income - expense
        })
        
