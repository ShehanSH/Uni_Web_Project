from django.contrib import admin
from .forms import InventoryCreateForm   
from .models import *



# Register your models here

from .models import Inventory_Stock

class InventoryCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity']
    form = InventoryCreateForm
    list_filter = ['category']
    search_fields = ['category', 'item_name', 'quantity']
    # list_editable = ['quantity']
    # class Meta:
    # 	model = Inventory_Stock


admin.site.register(Inventory_Stock, InventoryCreateAdmin)
admin.site.register(Category)



# Register your models here.

