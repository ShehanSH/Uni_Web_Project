from django.urls import path
from .views import create_sports_item_request, list_requests_view, update_sports_item_request

app_name = 'sports_items_req'

urlpatterns = [
    path('create_sports_item_request/', create_sports_item_request, name='create_sports_item_request'),
    # Add other URL patterns as needed
    path('list-requests/', list_requests_view, name='list_requests'),
    path('update-request/<int:request_id>/', update_sports_item_request, name='update_sports_item_request'),
]
