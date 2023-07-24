from django.contrib import admin
from .models import SportsItemRequest
from inventory_management.models import Inventory_Stock

class SportsItemRequestAdmin(admin.ModelAdmin):
    list_display = ['request_id', 'user', 'category', 'item', 'request_date', 'request_time', 'req_quantity', 'approval_status']
    list_filter = ['category', 'approval_status', 'user']
    actions = ['issue_sports_items']

   

# Register the admin class
admin.site.register(SportsItemRequest, SportsItemRequestAdmin)
