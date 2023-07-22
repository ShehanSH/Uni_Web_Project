
from django.urls import path
from .views import *
from django.urls import path
from . import views

app_name = 'ground_booking'

urlpatterns = [
    path('ground_booking_request/', ground_booking_request, name='ground_booking_request'),
    path('list_booking/', ground_booking_view, name='list_booking'),
    path('update_ground_booking_request/<str:pk>/', update_ground_booking_request, name="update_ground_booking_request"),
    path('delete_booking_request/<str:pk>/', delete_booking_request, name='delete_booking_request'),
    path('all_events/', all_events, name='all_events'),
    path('calendar/', calendar_view, name='calendar'),
    

]