from django.db import models
from accounts.models import CustomUser

class Ground(models.Model):
    ground_id = models.AutoField(primary_key=True)
    ground_name = models.CharField(max_length=255)
    area = models.CharField(max_length=100)
    booking_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.ground_name

class EventType(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)

    def __str__(self):
        return self.event_name

from django.db import models

class GroundBookingRequest(models.Model):
    APPROVAL_CHOICES = (
        ('A', 'Approval'),
        ('D', 'Disapproval'),
    )
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ground = models.ForeignKey(Ground, on_delete=models.CASCADE)
    request_date = models.DateField()
    request_time = models.TimeField()
    event = models.ForeignKey(EventType, on_delete=models.CASCADE)
    approval_status = models.CharField(max_length=1, choices=APPROVAL_CHOICES, default='D')
    event_form = models.ImageField(upload_to='ground_booking_forms/', null=True, blank=True)  # Add the image field

    def __str__(self):
        return f"Booking ID: {self.booking_id}, User: {self.user}, Ground: {self.ground}, Event: {self.event}"
