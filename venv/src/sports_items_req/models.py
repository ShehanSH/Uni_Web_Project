from django.db import models

# Create your models here.
from accounts.models import CustomUser
from inventory_management.models import Category, Inventory_Stock

from django.db import models
from inventory_management.models import Inventory_Stock

class SportsItemRequest(models.Model):
    APPROVAL_CHOICES = (
        ('A', 'Approval'),
        ('D', 'Disapproval'),
        ('I', 'Issued'),
    )
    request_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item = models.ForeignKey(Inventory_Stock, on_delete=models.CASCADE)
    request_date = models.DateField()
    request_time = models.TimeField()
    req_quantity = models.PositiveIntegerField()
    approval_status = models.CharField(max_length=1, choices=APPROVAL_CHOICES, default='D')

    def save(self, *args, **kwargs):
        # Check if the approval_status is changing to 'Issued' from a different value
        if self.pk and self.approval_status == 'I' and self._state.adding is False:
            # Get the Inventory_Stock object corresponding to the request's item
            inventory_item = Inventory_Stock.objects.get(item_id=self.item_id)

            # Calculate the new stock_quantity by reducing the req_quantity
            new_stock_quantity = inventory_item.stock_quantity - self.req_quantity
            if new_stock_quantity < 0:
                new_stock_quantity = 0  # Ensure stock_quantity doesn't go below 0

            # Update the stock_quantity in the Inventory_Stock model
            inventory_item.stock_quantity = new_stock_quantity
            inventory_item.save()

        super().save(*args, **kwargs)


class SportsItemReceived(models.Model):
    APPROVAL_CHOICES = (
        ('R', 'Recived'),
        ('N', 'Not Recived'),
        
    )
    ITEM_STATUS = (
        ('D', 'Damaged'),
        ('ND', 'Not Damaged'),
    )
    received_id = models.AutoField(primary_key=True)
    request_id = models.ForeignKey(SportsItemRequest, on_delete=models.CASCADE)
    item = models.ForeignKey(Inventory_Stock, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item = models.ForeignKey(Inventory_Stock, on_delete=models.CASCADE)
    received_date = models.DateField()
    received_time = models.TimeField()
    received_quantity = models.PositiveIntegerField()
    received_status = models.CharField(max_length=1, choices=APPROVAL_CHOICES, default='N')
    item_status = models.CharField(max_length=2, choices=ITEM_STATUS, default='ND')
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the recived item')

    