# inventory_management/tables.py
import django_tables2 as tables
from .models import Inventory_Stock

class InventoryStockTable(tables.Table):
    class Meta:
        model = Inventory_Stock
        fields = ('item_name', 'category', 'stock_quantity', 'reorder_level')
        template_name = 'django_tables2/bootstrap4.html'  # Use Bootstrap 4 styling for the table
