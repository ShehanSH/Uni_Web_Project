
from django.urls import path
from .views import *

app_name = 'ground_booking'

urlpatterns = [
    path('ground_booking_request/', ground_booking_request, name='ground_booking_request'),
    path('list_booking/', ground_booking_view, name='list_booking'),
]
