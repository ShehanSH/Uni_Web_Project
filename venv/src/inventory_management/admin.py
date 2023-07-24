# from django.contrib import admin
# from .forms import InventoryCreateForm   
# from .models import *





# # Register your models here

# # from .models import Inventory_Stock

# # class InventoryCreateAdmin(admin.ModelAdmin):
# #     list_display = ['category', 'item_name', 'quantity']
# #     form = InventoryCreateForm
# #     list_filter = ['category']
# #     search_fields = ['category', 'item_name', 'quantity']
# #     list_editable = ['quantity']
# #     class Meta:
# #     	model = Inventory_Stock


# # admin.site.register(Inventory_Stock, InventoryCreateAdmin)
# # admin.site.register(Category)

# from django.contrib import admin
# from .models import Inventory_Stock, Supplier
# from .forms import InventoryCreateForm, AddSupplierForm

# class Inventory_StockAdmin(admin.ModelAdmin):
#     form = InventoryCreateForm
#     list_display = ['item_name', 'quantity', 'reorder_level', 'price', 'Total_value', 'Supplier']

# class SupplierAdmin(admin.ModelAdmin):
#     form = AddSupplierForm
#     list_display = ['supplier_name', 'phone_number', 'email', 'address']

# admin.site.register(Inventory_Stock, Inventory_StockAdmin)
# admin.site.register(Supplier, SupplierAdmin)


# from django.contrib import admin
# from .models import IssueItem
# from .forms import IssueItemForm

# class IssueItemAdmin(admin.ModelAdmin):
#     form = IssueItemForm
#     list_display = ['item', 'issue_quantity', 'issue_by', 'issue_to']

# admin.site.register(IssueItem, IssueItemAdmin)


from django.contrib import admin
from .models import Category, Supplier, Inventory_Stock, Supply_Inventory
from .forms import SupplyInventoryForm

#supply inventory from supplers
class SupplyInventoryAdmin(admin.ModelAdmin):
    form = SupplyInventoryForm
    list_display = ['Supplier', 'category', 'item', 'supply_date', 'supply_time', 'supply_quantity', 'price', 'supply_total_value']
    search_fields = ['Supplier__supplier_name', 'category__name', 'item__item_name']
    list_filter = ['supply_date']

admin.site.register(Supply_Inventory, SupplyInventoryAdmin)

#supplers details
from django.contrib import admin
from .models import Supplier
from .forms import SupplierForm
class SupplierAdmin(admin.ModelAdmin):
    form = SupplierForm
    list_display = ['supplier_name', 'phone_number', 'email', 'address', 'company_name']
    search_fields = ['supplier_name', 'phone_number', 'email', 'address', 'company_name']
admin.site.register(Supplier, SupplierAdmin)

#category
from django.contrib import admin
from .models import Category
from .forms import CategoryForm
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ['category_id', 'name']
    search_fields = ['name']
admin.site.register(Category, CategoryAdmin)

#inventory stock
from .models import Inventory_Stock
from .forms import InventoryStockForm
class InventoryStockAdmin(admin.ModelAdmin):
    form = InventoryStockForm
    list_display = ['item_name', 'category', 'stock_quantity', 'reorder_level']
    search_fields = ['item_name']
    list_filter = ['category']


admin.site.register(Inventory_Stock, InventoryStockAdmin)
