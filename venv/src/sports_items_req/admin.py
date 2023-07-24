from django.contrib import admin
from .models import SportsItemRequest
from inventory_management.models import Inventory_Stock
from django.contrib import messages

class SportsItemRequestAdmin(admin.ModelAdmin):
    list_display = ['request_id', 'user', 'category', 'item', 'request_date', 'request_time', 'quantity', 'approval_status']
    list_filter = ['category', 'approval_status', 'user']
    actions = ['issue_sports_items']

    def has_change_permission(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return False
        return True

    def issue_sports_items(self, request, queryset):
        for obj in queryset:
            try:
                # Get the corresponding Inventory_Stock object for the requested item
                inventory_item = Inventory_Stock.objects.get(item_name=obj.item)

                # Check if the issue quantity exceeds the available quantity in the inventory
                if obj.quantity > inventory_item.quantity:
                    # Handle the case where the requested quantity exceeds the available quantity
                    # For example, you could reject the request or raise a notification.
                    messages.error(request, f"Cannot issue sports item. Stock has only {inventory_item.quantity} {inventory_item.item_name}s available.")
                else:
                    # Reduce the quantity in the inventory stock by the requested quantity
                    inventory_item.quantity -= obj.quantity
                    inventory_item.save()

                    # Update the SportsItemRequest object with the issue status and the user who issued it
                    obj.approval_status = 'ISSUED'
                    obj.issued_by = request.user
                    obj.save()

                    messages.success(request, f"Issued {obj.quantity} {obj.item} SUCCESSFULLY. {inventory_item.quantity} {obj.item} now left in Store")

            except Inventory_Stock.DoesNotExist:
                # Handle the case where the requested item is not found in the inventory
                messages.error(request, f"Cannot issue sports item. {obj.item} is not found in the inventory.")
        
    issue_sports_items.short_description = "Issue selected sports items"

# Register the SportsItemRequest model with the custom admin class
admin.site.register(SportsItemRequest, SportsItemRequestAdmin)
