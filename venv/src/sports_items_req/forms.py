from django import forms
from .models import SportsItemRequest, SportsItemReceived

class SportsItemsRequestForm(forms.ModelForm):
    class Meta:
        model = SportsItemRequest
        fields = ('category', 'item', 'request_date', 'request_time', 'req_quantity')
        widgets = {
            'category': forms.Select(attrs={'class': 'abc'}),
            'item': forms.Select(attrs={'class': 'abc'}),
            'request_date': forms.DateInput(attrs={'class': 'abc', 'type': 'date'}),
            'request_time': forms.TimeInput(attrs={'class': 'abc', 'type': 'time'}),
            'req_quantity': forms.NumberInput(attrs={'class': 'abc'}),
        }


class SportsItemRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = SportsItemRequest
        fields = ('category', 'item', 'request_date', 'request_time', 'req_quantity')
        widgets = {
            'category': forms.Select(attrs={'class': 'abc'}),
            'item': forms.Select(attrs={'class': 'abc'}),
            'request_date': forms.DateInput(attrs={'class': 'abc', 'type': 'date'}),
            'request_time': forms.TimeInput(attrs={'class': 'abc', 'type': 'time'}),
            'quantity': forms.NumberInput(attrs={'class': 'abc'}),
        }

from accounts.models import CustomUser
from inventory_management.models import Category, Inventory_Stock

class SportsItemReceivedForm(forms.ModelForm):
    class Meta:
        model = SportsItemReceived
        fields = ('request_id', 'user', 'category', 'item', 'received_date', 'received_time', 'received_quantity', 'received_status', 'item_status', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.request_id:
            # If the form is being used to update an existing instance, set the queryset
            # of 'user', 'category', and 'item' fields based on the 'request_id' value.
            request_id = instance.request_id
            self.fields['user'].queryset = CustomUser.objects.filter(sportsitemrequest__request_id=request_id)
            self.fields['category'].queryset = Category.objects.filter(sportsitemrequest__request_id=request_id)
            self.fields['item'].queryset = Inventory_Stock.objects.filter(sportsitemrequest__request_id=request_id)

       