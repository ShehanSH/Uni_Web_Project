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
            'req_quantity': forms.NumberInput(attrs={'class': 'abc'}),
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

   
# forms.py
from django import forms
from .models import SportsItemRequest,Category

# forms.py
from django import forms
from .models import SportsItemRequest

# class SportsItemReqStatusForm(forms.Form):
#     APPROVAL_CHOICES = (
#         ('', 'All'),  # Empty option for 'All' category
#         ('A', 'Approval'),
#         ('D', 'Disapproval'),
#         ('I', 'Issued'),
#     )

#     category = forms.ModelChoiceField(
#         queryset=Category.objects.all(),
#         empty_label="All",
#         required=False,
#         widget=forms.Select(attrs={'class': 'form-control form-control-inline'})
#     )
#     start_date = forms.DateField(
#         label='Start Date',
#         required=False,
#         widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-inline'})
#     )
#     end_date = forms.DateField(
#         label='End Date',
#         required=False,
#         widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-inline'})
#     )
#     approval_status = forms.ChoiceField(
#         choices=APPROVAL_CHOICES,
#         required=False,
#         widget=forms.Select(attrs={'class': 'form-control form-control-inline'})
#     )


# forms.py
from django import forms
from .models import Category, SportsItemRequest

from django import forms
from .models import Category

from django import forms
from .models import Category
from django import forms
from .models import Category

class ItemRequestFilterForm(forms.Form):
    start_date = forms.DateField(
        label='Start Date',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-inline'})
    )
    end_date = forms.DateField(
        label='End Date',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-inline'})
    )
    categories = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="All",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )


from django import forms

from django import forms
from .models import Category

# class SportsItemRequestFilterForm(forms.Form):
#     categories = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="All", required=False, widget=forms.Select(attrs={'class': 'form-control'}))
#     start_date = forms.DateField(label='Start Date', required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-inline'}))
#     end_date = forms.DateField(label='End Date', required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-inline'}))
class SportsItemRequestReceivedFilterForm(forms.Form):
    categories = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="All", required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    start_date = forms.DateField(label='Start Date', required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-inline'}))
    end_date = forms.DateField(label='End Date', required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-inline'}))

from django import forms
from .models import Category

class SportsItemRequestStackedFilterForm(forms.Form):
    categories = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="All", required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    start_date = forms.DateField(label='Start Date', required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-inline'}))
    end_date = forms.DateField(label='End Date', required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-inline'}))


