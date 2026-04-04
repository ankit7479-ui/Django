from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from users.permissions import IsAdmin, IsAnalystOrAdmin

# Create your views here.
class FinancialRecordViewSet(ModelViewSet):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdmin()]
        elif self.action in ['list', 'retrieve']:
            return [IsAnalystOrAdmin()]
        return []
    
    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtering
        type = self.request.query_params.get('type')
        category = self.request.query_params.get('category')

        if type:
            queryset = queryset.filter(type=type)
        if category:
            queryset = queryset.filter(category=category)

        return queryset