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
    list_display = ['Supplier', 'category', 'item', 'supply_date', 'supply_time', 'supply_quantity']
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
from django.contrib import admin
from inventory_management.models import Inventory_Stock

class DamageQuantityFilter(admin.SimpleListFilter):
    title = 'Damage Quantity'
    parameter_name = 'damage_quantity__gt'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Has Damage'),  # Display 'Has Damage' as a filter option
            ('0', 'No Damage'),   # Display 'No Damage' as a filter option
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == '1':
            return queryset.exclude(damage_quantity__exact=0)
        elif value == '0':
            return queryset.filter(damage_quantity__exact=0)


class LostQuantityFilter(admin.SimpleListFilter):
    title = 'Lost Quantity'
    parameter_name = 'lost_quantity__gt'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Has Lost'),  # Display 'Has Lost' as a filter option
            ('0', 'No Lost'),   # Display 'No Lost' as a filter option
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == '1':
            return queryset.exclude(lost_quantity__exact=0)
        elif value == '0':
            return queryset.filter(lost_quantity__exact=0)


from django.contrib import admin
from django.utils.html import format_html

class InventoryStockAdmin(admin.ModelAdmin):
    form = InventoryStockForm
    list_display = ['item_name', 'category', 'display_stock_quantity', 'damage_quantity', 'lost_quantity', 'reorder_level']
    search_fields = ['item_name']
    list_filter = ['category', DamageQuantityFilter, LostQuantityFilter]

    def display_stock_quantity(self, obj):
        if obj.stock_quantity < obj.reorder_level:
            return format_html('<span style="color: red; background-color:yellow;">{}</span>', obj.stock_quantity)
        return obj.stock_quantity

    display_stock_quantity.short_description = 'Stock Quantity'






admin.site.register(Inventory_Stock, InventoryStockAdmin)
