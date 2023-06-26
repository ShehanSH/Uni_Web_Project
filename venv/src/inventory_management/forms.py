from django import forms
from .models import Inventory_Stock

class InventoryCreateForm(forms.ModelForm):
    class Meta:
        model = Inventory_Stock
        fields = ['category', 'item_name', 'quantity']

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')
        # for category_name in Inventory_Stock.objects.all():
        #     if category_name.category == category:
        #         raise forms.ValidationError(category + ' is already created')
        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')
        for item in Inventory_Stock.objects.all():
            if item.item_name == item_name:
                raise forms.ValidationError(item_name + ' is already created')
        return item_name



class InventorySearchForm(forms.ModelForm):
    category = forms.CharField(max_length=50, required=False)
    item_name = forms.CharField(max_length=50, required=False)
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Inventory_Stock
        fields = ['category', 'item_name']

class InventoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Inventory_Stock
        fields = ['category', 'item_name', 'quantity']

class IssueForm(forms.ModelForm):
    class Meta:
        model = Inventory_Stock
        fields = ['issue_quantity', 'issue_to']    
        # add to issue by

class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Inventory_Stock
        fields = ['receive_quantity']    

class ReorderLevelForm(forms.ModelForm):
	class Meta:
		model = Inventory_Stock
		fields = ['reorder_level']