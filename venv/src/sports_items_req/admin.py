from django.contrib import admin
from .models import SportsItemRequest

class SportsItemRequestAdmin(admin.ModelAdmin):
    list_display = ['request_id', 'user', 'category', 'item', 'request_date', 'request_time', 'quantity', 'approval_status']
    list_filter = ['category', 'approval_status']

    def has_change_permission(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return False
        return True

admin.site.register(SportsItemRequest, SportsItemRequestAdmin)



