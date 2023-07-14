from django.db import models

# Create your models here.
from accounts.models import CustomUser
from inventory_management.models import Category, Inventory_Stock

class SportsItemRequest(models.Model):
    APPROVAL_CHOICES = (
        ('A', 'Approval'),
        ('D', 'Disapproval'),
    )
    request_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item = models.ForeignKey(Inventory_Stock, on_delete=models.CASCADE)
    request_date = models.DateField()
    request_time = models.TimeField()
    quantity = models.PositiveIntegerField()
    approval_status = models.CharField(max_length=1, choices=APPROVAL_CHOICES, default='D')



 