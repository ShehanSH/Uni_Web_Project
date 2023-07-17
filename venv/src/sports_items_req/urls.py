from django.urls import path
from .views import create_sports_item_request, list_requests_view, update_sports_item_request
from .views import *

app_name = 'sports_items_req'

urlpatterns = [
    path('create_sports_item_request/', create_sports_item_request, name='create_sports_item_request'),
    # Add other URL patterns as needed
    path('list_requests/', list_requests_view, name='list_requests'),
    # path('update_sports_item_request/<int:request_id>/', update_sports_item_request, name='update_sports_item_request'),
    path('update_sports_item_request/<str:pk>/', update_sports_item_request, name="update_sports_item_request"),
    path('delete_request/<str:pk>/', delete_request, name='delete_request'),
]
