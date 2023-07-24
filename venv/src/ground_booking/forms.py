from django import forms
from .models import Ground, EventType,GroundBookingRequest


class GroundBookingRequestForm(forms.ModelForm):
    # ground = forms.ModelChoiceField(queryset=Ground.objects.all(), widget=forms.Select(attrs={'class': 'abc'}))
    # event = forms.ModelChoiceField(queryset=EventType.objects.all(), widget=forms.Select(attrs={'class': 'abc'}))

    class Meta:
        model = GroundBookingRequest
        fields = ('request_date', 'request_time', 'ground', 'event', 'event_form')
        widgets = {
            'request_date': forms.DateInput(attrs={'class': 'abc', 'type': 'date'}),
            'request_time': forms.TimeInput(attrs={'class': 'abc', 'type': 'time'}),
            'ground': forms.Select(attrs={'class': 'abc'}),
            'event': forms.Select(attrs={'class': 'abc'}),
            'event_form': forms.ClearableFileInput(attrs={'class': 'abc', 'type': 'file'}),
        }


class GroundBookingRequestUpdateForm(forms.ModelForm):
    # ground = forms.ModelChoiceField(queryset=Ground.objects.all(), widget=forms.Select(attrs={'class': 'abc'}))
    # event = forms.ModelChoiceField(queryset=EventType.objects.all(), widget=forms.Select(attrs={'class': 'abc'}))

    class Meta:
        model = GroundBookingRequest
        fields = ('request_date', 'request_time', 'ground', 'event', 'event_form')
        widgets = {
            'request_date': forms.DateInput(attrs={'class': 'abc', 'type': 'date'}),
            'request_time': forms.TimeInput(attrs={'class': 'abc', 'type': 'time'}),
            'ground': forms.Select(attrs={'class': 'abc'}),
            'event': forms.Select(attrs={'class': 'abc'}),
            'event_form': forms.ClearableFileInput(attrs={'class': 'abc', 'type': 'file'}),
        }
