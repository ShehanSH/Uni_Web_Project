from django import forms
from .models import Inventory_Stock, Inventory_Stock_History
from accounts.models import CustomUser
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


# inventory search form related to the list_items.html
class InventorySearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Inventory_Stock
        fields = ['category', 'item_name']


# inventory history search form related to the list_history.html

class InventoryStockHistorySearchForm(forms.ModelForm):
	export_to_CSV = forms.BooleanField(required=False)
	start_date = forms.DateTimeField(required=False)
	end_date = forms.DateTimeField(required=False)
	class Meta:
		model = Inventory_Stock_History
		fields = ['category', 'item_name', 'start_date', 'end_date']
                

class InventoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Inventory_Stock
        fields = ['category', 'item_name', 'quantity']

class IssueForm(forms.ModelForm):
    issue_to = forms.ModelChoiceField(queryset=CustomUser.objects.all(), label='Issue To')
    class Meta:
        model = Inventory_Stock
        fields = ['issue_quantity', 'issue_to']    
        # add to issue by
    def __init__(self, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        self.fields['issue_to'].widget.attrs['data-ajax--url'] = '/search_users/'   

class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Inventory_Stock
        fields = ['receive_quantity']    

class ReorderLevelForm(forms.ModelForm):
	class Meta:
		model = Inventory_Stock
		fields = ['reorder_level']