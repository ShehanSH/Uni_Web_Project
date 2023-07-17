from django.contrib import admin
from .models import GroundBookingRequest, Ground, EventType


class GroundAdmin(admin.ModelAdmin):
    list_display = ['ground_id', 'ground_name', 'area', 'booking_price']
    search_fields = ['ground_name', 'area']

class EventTypeAdmin(admin.ModelAdmin):
    list_display = ['event_id', 'event_name']
    search_fields = ['event_name']

class GroundBookingRequestAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'user', 'ground', 'request_date', 'request_time', 'event', 'approval_status']
    list_filter = ['approval_status', 'event']
    search_fields = ['user__username']

    def has_change_permission(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return False
        return True


admin.site.register(Ground, GroundAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(GroundBookingRequest, GroundBookingRequestAdmin)
