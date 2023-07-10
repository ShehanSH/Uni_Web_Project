from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ValidationError
from inventory_management.models import Category, Inventory_Stock

from django.conf import settings
from django.db import models


# Create your models here.
class SportsItemReq(models.Model):
     
    item_id = models.ForeignKey(Inventory_Stock, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    req_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    required_date = models.DateField()
    required_time = models.TimeField()

    PURPOSE_CHOICES = [
        ('university', 'For competition in university'),
        ('outside', 'For competition outside university'),
    ]
    purpose = models.CharField(max_length=10, choices=PURPOSE_CHOICES)
   

