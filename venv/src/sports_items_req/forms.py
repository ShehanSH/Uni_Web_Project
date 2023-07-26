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




from django import forms
from .models import SportsItemReceived

from django import forms
from .models import SportsItemReceived

from django import forms
from .models import SportsItemReceived

class SportsItemReceivedForm(forms.ModelForm):
    class Meta:
        model = SportsItemReceived
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the request_id choices to only include SportsItemRequest IDs with approval_status 'Issued'
        self.fields['request_id'].queryset = self.fields['request_id'].queryset.filter(approval_status='I')

   
