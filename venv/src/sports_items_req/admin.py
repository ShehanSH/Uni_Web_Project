from django.contrib import admin
from .models import SportsItemRequest
from inventory_management.models import Inventory_Stock

class SportsItemRequestAdmin(admin.ModelAdmin):
    list_display = ['request_id', 'user', 'category', 'item', 'request_date', 'request_time', 'quantity', 'approval_status']
    list_filter = ['category', 'approval_status', 'user']

    def has_change_permission(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return False
        return True

    def save_model(self, request, obj, form, change):
        # Save the model to database first
        obj.save()

        # If the request is approved and the admin is not updating the object
        if obj.approval_status == 'APPROVED' and not change:
            try:
                # Get the corresponding Inventory_Stock object for the requested item
                inventory_item = Inventory_Stock.objects.get(item_name=obj.item)

                # Reduce the quantity in the inventory stock by the requested quantity
                inventory_item.quantity -= obj.quantity
                inventory_item.save()

                # Here, you can also add additional logic to handle cases where the requested quantity
                # exceeds the available quantity in the inventory or handle any other business rules.

            except Inventory_Stock.DoesNotExist:
                # Handle the case where the requested item is not found in the inventory
                pass


admin.site.register(SportsItemRequest, SportsItemRequestAdmin)



