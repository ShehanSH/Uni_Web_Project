from django.db import models



from django.db import models
from .models import CustomUser, Category

from django.db import models
from .models import CustomUser, Ground

class GroundBookingRequest(models.Model):
    APPROVAL_CHOICES = (
        ('A', 'Approval'),
        ('D', 'Disapproval'),
    )
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ground = models.ForeignKey(Ground, on_delete=models.CASCADE)  # Add the ground_id as a foreign key
    request_date = models.DateField()
    request_time = models.TimeField()
    event_type = models.CharField(max_length=255)
    approval_status = models.CharField(max_length=1, choices=APPROVAL_CHOICES, default='D')



class Ground(models.Model):
    ground_id = models.AutoField(primary_key=True)
    ground_name = models.CharField(max_length=255)
    area = models.CharField(max_length=100)
    booking_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.ground_name
