from finance.models import FinancialRecord
from django.db.models import Sum

def get_summary(user):
    records = FinancialRecord.objects.filter(user=user)

    income = records.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    expense = records.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }