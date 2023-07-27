from django.contrib import admin
from .models import SportsItemRequest, SportsItemReceived
from inventory_management.models import Inventory_Stock

class SportsItemRequestAdmin(admin.ModelAdmin):
    list_display = ['request_id', 'user', 'category', 'item', 'request_date', 'request_time', 'req_quantity', 'approval_status']
    list_filter = ['category', 'approval_status', 'user']
    actions = ['issue_sports_items']

   


from django.contrib import admin
from .models import SportsItemRequest, SportsItemReceived
from .forms import SportsItemsRequestForm, SportsItemRequestUpdateForm, SportsItemReceivedForm

class SportsItemReceivedAdmin(admin.ModelAdmin):
    list_display = ['request_id', 'user', 'category', 'item', 'received_date', 'received_time', 'received_quantity', 'damage_quantity','received_status', 'item_status', 'description']
    list_filter = ['category', 'received_status', 'item_status', 'user', 'request_id']
    form = SportsItemReceivedForm


# Register the model with the custom admin class
admin.site.register(SportsItemReceived, SportsItemReceivedAdmin)





# Register the admin class
admin.site.register(SportsItemRequest, SportsItemRequestAdmin)

