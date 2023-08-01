from django.urls import path
from .views import *
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'ground_booking'
urlpatterns = [
    path('create_ground_booking_request/', create_ground_booking_request, name='create_ground_booking_request'),
    path('list_booking/', ground_booking_view, name='list_booking'),
    path('update_ground_booking_request/<str:pk>/', update_ground_booking_request, name="update_ground_booking_request"),
    path('delete_booking_request/<str:pk>/', delete_booking_request, name='delete_booking_request'),
    path('all_events/', all_events, name='all_events'),
    path('calendar/', calendar_view, name='calendar'),
    path('ground/details/', views.ground_details_view, name='ground_details'),

    #charts
    path('ground_booking_bar_chart/', views.ground_booking_bar_chart_view, name='ground_booking_bar_chart'),
    path('ground_booking_stacked_bar_chart/', views.ground_booking_stacked_bar_chart_view, name='ground_booking_stacked_bar_chart'),
    path('ground_booking_line_chart/', views.ground_booking_line_chart_view, name='ground_booking_line_chart'),

    #reports
    path('ground_booking_request/', views.ground_booking_request, name='ground_booking_request'),
    path('booking_summary/', views.booking_summary, name='booking_summary'),

    #booking receipt
    path('generate-booking-receipt-pdf/<int:booking_id>/', views.generate_booking_receipt_pdf, name='generate_booking_receipt_pdf'),
   
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
