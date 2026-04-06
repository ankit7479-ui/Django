from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('expenses/', ExpenseListCreateView.as_view()),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view()),
]