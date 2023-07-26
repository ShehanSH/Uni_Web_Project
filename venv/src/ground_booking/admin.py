from django.contrib import admin
from .models import GroundBookingRequest, Ground, EventType
from django.contrib import admin
from django.utils.html import format_html
from .models import GroundBookingRequest

class GroundAdmin(admin.ModelAdmin):
    list_display = ['ground_id', 'ground_name', 'area', 'booking_price', 'ground_image']
    search_fields = ['ground_name', 'area']
    list_display_links = ['ground_name'] 
    
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ['event_id', 'event_name']
    search_fields = ['event_name']

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
    list_display = ['booking_id', 'user', 'ground', 'request_date', 'request_time', 'event', 'display_payment_form', 'display_payment_receipt','approval_status' ]
    list_filter = ['approval_status', 'event', EventFormFilter]
    search_fields = ['user__username']

    def has_change_permission(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return False
        return True

    def display_payment_form(self, obj):
        if obj.event_form:
            return format_html('<a href="{}" download target="_blank">Event Form Download</a>', obj.event_form.url)
        else:
            return 'Not Submitted'
    display_payment_form.short_description = 'Event Form'

    def display_payment_receipt(self, obj):
        if obj.payment_receipt:
            return format_html('<a href="{}" download target="_blank">Payment Receipt Download</a>', obj.payment_receipt.url)
        else:
            return 'Not Submitted'
    display_payment_receipt.short_description = 'Payment Receipt'



# Register the model with the custom admin
admin.site.register(GroundBookingRequest, GroundBookingRequestAdmin)
admin.site.register(Ground, GroundAdmin)
admin.site.register(EventType, EventTypeAdmin)

