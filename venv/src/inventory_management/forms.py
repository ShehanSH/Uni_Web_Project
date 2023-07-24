# # from django import forms
# # from .models import Inventory_Stock, Inventory_Stock_History
# # from accounts.models import CustomUser
# # class InventoryCreateForm(forms.ModelForm):
# #     class Meta:
# #         model = Inventory_Stock
# #         fields = ['category', 'item_name', 'quantity']

# #     def clean_category(self):
# #         category = self.cleaned_data.get('category')
# #         if not category:
# #             raise forms.ValidationError('This field is required')
# #         # for category_name in Inventory_Stock.objects.all():
# #         #     if category_name.category == category:
# #         #         raise forms.ValidationError(category + ' is already created')
# #         return category

# #     def clean_item_name(self):
# #         item_name = self.cleaned_data.get('item_name')
# #         if not item_name:
# #             raise forms.ValidationError('This field is required')
# #         for item in Inventory_Stock.objects.all():
# #             if item.item_name == item_name:
# #                 raise forms.ValidationError(item_name + ' is already created')
# #         return item_name


# # # inventory search form related to the list_items.html
# # class InventorySearchForm(forms.ModelForm):
# #     export_to_CSV = forms.BooleanField(required=False)
# #     class Meta:
# #         model = Inventory_Stock
# #         fields = ['category', 'item_name']


# # # inventory history search form related to the list_history.html

# # class InventoryStockHistorySearchForm(forms.ModelForm):
# # 	export_to_CSV = forms.BooleanField(required=False)
# # 	start_date = forms.DateTimeField(required=False)
# # 	end_date = forms.DateTimeField(required=False)
# # 	class Meta:
# # 		model = Inventory_Stock_History
# # 		fields = ['category', 'item_name', 'start_date', 'end_date']
                

# # class InventoryUpdateForm(forms.ModelForm):
# #     class Meta:
# #         model = Inventory_Stock
# #         fields = ['category', 'item_name', 'quantity']

# # class IssueForm(forms.ModelForm):
# #     issue_to = forms.ModelChoiceField(queryset=CustomUser.objects.all(), label='Issue To')
# #     class Meta:
# #         model = Inventory_Stock
# #         fields = ['issue_quantity', 'issue_to']    
# #         # add to issue by
# #     def __init__(self, *args, **kwargs):
# #         super(IssueForm, self).__init__(*args, **kwargs)
# #         self.fields['issue_to'].widget.attrs['data-ajax--url'] = '/search_users/'   

# # class ReceiveForm(forms.ModelForm):
# #     class Meta:
# #         model = Inventory_Stock
# #         fields = ['receive_quantity']    

# # class ReorderLevelForm(forms.ModelForm):
# # 	class Meta:
# # 		model = Inventory_Stock
# # 		fields = ['reorder_level']



# from django import forms
# from .models import Supplier

# class AddSupplierForm(forms.ModelForm):
#     class Meta:
#         model = Supplier
#         fields = ['supplier_name', 'phone_number', 'email', 'address']
     
# from django import forms
# from .models import Supplier

# from django import forms
# from .models import Inventory_Stock


# from django import forms
# from .models import Inventory_Stock


 
# # from django import forms
# # from .models import IssueItem

# # from django import forms
# # from .models import IssueItem

# # from django import forms
# # from .models import IssueItem

# # class IssueItemForm(forms.ModelForm):
# #     CHOICES = (
# #         ('admin', 'Admin'),
# #     )

# #     issue_by = forms.ChoiceField(choices=CHOICES)
# #     issue_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
# #     issue_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

# #     class Meta:
# #         model = IssueItem
# #         fields = ['category', 'item', 'issue_quantity', 'issue_by', 'issue_to', 'issue_date', 'issue_time']

# #     def __init__(self, *args, **kwargs):
# #         super(IssueItemForm, self).__init__(*args, **kwargs)
# #         if self.instance.item:
# #             available_quantity = self.instance.item.quantity
# #             self.fields['issue_quantity'].widget = forms.NumberInput(attrs={'value': available_quantity})
# #             self.fields['issue_quantity'].disabled = True


from django import forms
from .models import Supply_Inventory, Supplier, Inventory_Stock, Category

class SupplyInventoryForm(forms.ModelForm):
    class Meta:
        model = Supply_Inventory
        fields = ['Supplier', 'category', 'item', 'supply_date', 'supply_time', 'supply_quantity', 'price']

    def __init__(self, *args, **kwargs):
        super(SupplyInventoryForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = Inventory_Stock.objects.all()


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier_name', 'phone_number', 'email', 'address', 'company_name']

from django import forms
from .models import Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_id', 'name']

from .models import Inventory_Stock
class InventoryStockForm(forms.ModelForm):
    class Meta:
        model = Inventory_Stock
        fields = ['category', 'item_name', 'stock_quantity', 'reorder_level']
