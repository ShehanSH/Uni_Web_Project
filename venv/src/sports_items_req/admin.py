from django.contrib import admin
from .models import SportsItemRequest

class SportsItemRequestAdmin(admin.ModelAdmin):
    list_display = ['request_id', 'user', 'category', 'item', 'request_date', 'request_time', 'quantity', 'approval_status']
    list_filter = ['category', 'approval_status']
    readonly_fields = ['request_id', 'user', 'category', 'item', 'request_date', 'request_time', 'quantity']

    def get_readonly_fields(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return self.readonly_fields + ['approval_status']
        return self.readonly_fields

    def has_change_permission(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return False
        return True

admin.site.register(SportsItemRequest, SportsItemRequestAdmin)
