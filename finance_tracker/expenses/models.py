from django.db import models
from django.conf import settings

# Create your models here.
class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
