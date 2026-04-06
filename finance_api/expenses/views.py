from .models import Expense
from .serializers import RegisterSerializer, ExpenseSerializer
from rest_framework import generics, permissions
# Create your views here.

# Register Api
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    
 # # List + Create
class ExpenseListCreateView(generics.ListCreateAPIView):
        serializer_class = ExpenseSerializer
        permission_classes = [permissions.IsAuthenticated]
        
        def get_queryset(self):
              return Expense.objects.filter(user=self.request.user)
          
        def perform_create(self, serializer):
              serializer.save(user=self.request.user)
              
# Detail API

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
          return Expense.objects.filter(user=self.request.user)