from django import forms
from .models import GroundBookingRequest
class GroundBookingRequestForm(forms.ModelForm):
    # ground = forms.ModelChoiceField(queryset=Ground.objects.all(), widget=forms.Select(attrs={'class': 'abc'}))
    # event = forms.ModelChoiceField(queryset=EventType.objects.all(), widget=forms.Select(attrs={'class': 'abc'}))

    class Meta:
        model = GroundBookingRequest
        fields = ('request_date', 'request_time', 'ground', 'event', 'event_form', 'payment_receipt')
        widgets = {
            'request_date': forms.DateInput(attrs={'class': 'abc', 'type': 'date'}),
            'request_time': forms.TimeInput(attrs={'class': 'abc', 'type': 'time'}),
            'ground': forms.Select(attrs={'class': 'abc'}),
            'event': forms.Select(attrs={'class': 'abc'}),
            'event_form': forms.ClearableFileInput(attrs={'class': 'abc', 'type': 'file'}),
            'payment_receipt': forms.ClearableFileInput(attrs={'class': 'abc', 'type': 'file'}),
        }


class GroundBookingRequestUpdateForm(forms.ModelForm):
    # ground = forms.ModelChoiceField(queryset=Ground.objects.all(), widget=forms.Select(attrs={'class': 'abc'}))
    # event = forms.ModelChoiceField(queryset=EventType.objects.all(), widget=forms.Select(attrs={'class': 'abc'}))

    class Meta:
        model = GroundBookingRequest
        fields = ('request_date', 'request_time', 'ground', 'event', 'event_form', 'payment_receipt')
        widgets = {
            'request_date': forms.DateInput(attrs={'class': 'abc', 'type': 'date'}),
            'request_time': forms.TimeInput(attrs={'class': 'abc', 'type': 'time'}),
            'ground': forms.Select(attrs={'class': 'abc'}),
            'event': forms.Select(attrs={'class': 'abc'}),
            'event_form': forms.ClearableFileInput(attrs={'class': 'abc', 'type': 'file'}),
            'payment_receipt': forms.ClearableFileInput(attrs={'class': 'abc', 'type': 'file'}),
        }


from django import forms
from .models import Ground

class GroundBookingFilterForm(forms.Form):
    start_date = forms.DateField(label='Start Date', required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-inline'}))
    end_date = forms.DateField(label='End Date', required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-inline'}))
    ground_name = forms.ModelChoiceField(queryset=Ground.objects.all(), empty_label="All", required=False, widget=forms.Select(attrs={'class': 'form-control'}))
