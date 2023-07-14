from django import forms
from .models import SportsItemRequest

class SportsItemsRequestForm(forms.ModelForm):
    class Meta:
        model = SportsItemRequest
        fields = ('category', 'item', 'request_date', 'request_time', 'quantity')
        widgets = {
            'category': forms.Select(attrs={'class': 'abc'}),
            'item': forms.Select(attrs={'class': 'abc'}),
            'request_date': forms.DateInput(attrs={'class': 'abc', 'type': 'date'}),
            'request_time': forms.TimeInput(attrs={'class': 'abc', 'type': 'time'}),
            'quantity': forms.NumberInput(attrs={'class': 'abc'}),
        }


