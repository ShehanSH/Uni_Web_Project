from django import forms
from .models import Inventory_Stock

class InventoryCreateForm(forms.ModelForm):
    class Meta:
        model =  Inventory_Stock
        fields = ['category', 'item_name', 'quantity']