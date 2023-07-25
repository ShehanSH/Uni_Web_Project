from django.contrib import admin
from .models import GroundBookingRequest, Ground, EventType


class GroundAdmin(admin.ModelAdmin):
    list_display = ['ground_id', 'ground_name', 'area', 'booking_price']
    search_fields = ['ground_name', 'area']

class EventTypeAdmin(admin.ModelAdmin):
    list_display = ['event_id', 'event_name']
    search_fields = ['event_name']

from django.contrib import admin
from django.utils.html import format_html
from .models import GroundBookingRequest

class EventFormFilter(admin.SimpleListFilter):
    title = 'Event Form Submitted'
    parameter_name = 'event_form_submitted'

    def lookups(self, request, model_admin):
        return (
            ('submitted', 'Submitted'),
            ('not_submitted', 'Not Submitted'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'submitted':
            return queryset.exclude(event_form__exact='')
        elif self.value() == 'not_submitted':
            return queryset.filter(event_form__exact='')
        return queryset

class GroundBookingRequestAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'user', 'ground', 'request_date', 'request_time', 'event', 'display_event_form', 'approval_status']
    list_filter = ['approval_status', 'event', EventFormFilter]
    search_fields = ['user__username']

    def has_change_permission(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return False
        return True

    def display_event_form(self, obj):
        if obj.event_form:
            return format_html('<a href="{}" download target="_blank">Event Form Download</a>', obj.event_form.url)
        else:
            return 'Not Submitted'
    display_event_form.short_description = 'Event Form'

# Register the model with the custom admin
admin.site.register(GroundBookingRequest, GroundBookingRequestAdmin)


admin.site.register(Ground, GroundAdmin)
admin.site.register(EventType, EventTypeAdmin)

