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
    TYPE_CHOICES = (
        ('P', 'Practise'),
        ('T', 'Tournament'),
    )
    request_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    item = models.ForeignKey(Inventory_Stock, on_delete=models.CASCADE, null=False, blank=False)
    request_date = models.DateField(null=False, blank=False)
    request_time = models.TimeField(null=False, blank=False)
    req_quantity = models.PositiveIntegerField(null=False, blank=False)
    request_type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='P', null=False, blank=False)
    approval_status = models.CharField(max_length=1, choices=APPROVAL_CHOICES, default='D', null=False, blank=False)



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
    DAMAGE_STATUS = (
        ('D', 'Damaged'),
        ('ND', 'No Damaged'),
        
    )

    LOST_STATUS = (
        ('L', 'Lost'),
        ('NL', 'No Losted'),    
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
    damage_quantity = models.PositiveIntegerField(null=True,  blank=True, default=0)
    lost_quantity = models.PositiveIntegerField(null=True,  blank=True, default=0)
    received_status = models.CharField(max_length=1, choices=APPROVAL_CHOICES, default='N')
    damage_status = models.CharField(max_length=2, choices=DAMAGE_STATUS, default='ND')
    lost_status = models.CharField(max_length=2, choices=LOST_STATUS, default='NL')
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the received item', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.received_status == 'R':  # Check if the received_status is 'Recived'
            # Get the Inventory_Stock object corresponding to the received item
            inventory_item = Inventory_Stock.objects.get(item_id=self.item_id)

            # Calculate the new stock_quantity by adding the received_quantity
            new_stock_quantity = inventory_item.stock_quantity + self.received_quantity

            # Update the fields in the Inventory_Stock model
            inventory_item.stock_quantity = new_stock_quantity

            if self.damage_status == 'D':  # Check if damage_status is 'Damaged'
                # Calculate the new damage_quantity for Inventory_Stock
                new_damage_quantity = inventory_item.damage_quantity + self.damage_quantity
                inventory_item.damage_quantity = new_damage_quantity

            if self.lost_status == 'L':  # Check if lost_status is 'Lost'
                # Calculate the new lost_quantity for Inventory_Stock
                new_lost_quantity = inventory_item.lost_quantity + self.lost_quantity
                inventory_item.lost_quantity = new_lost_quantity

            inventory_item.save()

        super().save(*args, **kwargs)