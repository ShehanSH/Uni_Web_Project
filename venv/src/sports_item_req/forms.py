from django import forms
from .models import Category, Inventory_Stock
from django.contrib.auth import get_user_model
from django import forms
from django.apps import apps

SportsItemReq = apps.get_model('sports_item_req', 'SportsItemReq')




User = get_user_model()

class SportsItemReqForm(forms.ModelForm):
    quantity = forms.IntegerField(label='Quantity')
    required_date = forms.DateField(label='Required Date')
    required_time = forms.TimeField(label='Required Time')
    # user_id = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())
    user_id = forms.DateField(label='User ID')

    PURPOSE_CHOICES = [
        ('university', 'For competition in university'),
        ('outside', 'For competition outside university'),
    ]
    purpose = forms.ChoiceField(label='Purpose', choices=PURPOSE_CHOICES, widget=forms.Select(attrs={'class': 'abc'}))

    item_name = forms.ChoiceField(label='Item Name', choices=[])  # Choices will be populated dynamically
    item_category = forms.ChoiceField(label='Item Category', choices=[])  # Choices will be populated dynamically

    class Meta:
        model = SportsItemReq
        fields = ['quantity', 'required_date', 'required_time', 'purpose', 'item_name', 'item_category', 'user_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_category'].choices = self.get_category_choices()
        self.fields['item_name'].choices = self.get_item_choices()

    def get_category_choices(self):
        categories = Category.objects.all()
        choices = [(category.category_id, category.name) for category in categories]

        return choices

    def get_item_choices(self):
        items = Inventory_Stock.objects.all()
        choices = [(item.item_id, item.item_name) for item in items]

        return choices
