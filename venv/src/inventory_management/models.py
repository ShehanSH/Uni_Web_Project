from django.db import models
from django.db import models

class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return self.name

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.supplier_name


class Inventory_Stock(models.Model):
    item_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    stock_quantity = models.IntegerField(default=0, blank=True, null=True)
    damage_quantity = models.IntegerField(default=0, blank=True, null=True)
    lost_quantity = models.IntegerField(default=0, blank=True, null=True)
    reorder_level = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.item_name

        

class Supply_Inventory(models.Model):
    Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    supply_date = models.DateField(blank=True, null=True)
    supply_time = models.TimeField(blank=True, null=True)
    item = models.ForeignKey(Inventory_Stock, on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    supply_quantity = models.IntegerField(default=0, blank=True, null=True)
    

    def __str__(self):
        return f"{self.item.item_name} ({self.supply_quantity})"

    def save(self, *args, **kwargs):
        

        # Get the corresponding Inventory_Stock object
        inventory_stock = self.item

        # Calculate the updated stock_quantity
        updated_stock_quantity = inventory_stock.stock_quantity + self.supply_quantity

        # Update the stock_quantity field of the Inventory_Stock object
        inventory_stock.stock_quantity = updated_stock_quantity
        inventory_stock.save()

        super(Supply_Inventory, self).save(*args, **kwargs)





# class Inventory_Stock(models.Model):
# 	item_id = models.AutoField(primary_key=True)
# 	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
# 	item_name = models.CharField(max_length=50, blank=True, null=True)
# 	quantity = models.IntegerField(default='0', blank=True, null=True)
# 	# receive_quantity = models.IntegerField(default='0', blank=True, null=True)
# 	# issue_quantity = models.IntegerField(default='0', blank=True, null=True)
# 	# issue_by = models.CharField(max_length=50, blank=True, null=True)
# 	# issue_to = models.CharField(max_length=50, blank=True, null=True)
# 	# phone_number = models.CharField(max_length=50, blank=True, null=True)
# 	# created_by = models.CharField(max_length=50, blank=True, null=True)
# 	reorder_level = models.IntegerField(default='0', blank=True, null=True)
# 	Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
# 	# last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
# 	# timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	

# 	def __str__(self):
# 		return self.item_name + " " + str(self.quantity)


# class Inventory_Stock_History(models.Model):
# 	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
# 	item_name = models.CharField(max_length=50, blank=True, null=True)
# 	quantity = models.IntegerField(default='0', blank=True, null=True)
# 	receive_quantity = models.IntegerField(default='0', blank=True, null=True)
# 	receive_by = models.CharField(max_length=50, blank=True, null=True)
# 	issue_quantity = models.IntegerField(default='0', blank=True, null=True)
# 	issue_by = models.CharField(max_length=50, blank=True, null=True)
# 	issue_to = models.CharField(max_length=50, blank=True, null=True)
# 	phone_number = models.CharField(max_length=50, blank=True, null=True)
# 	created_by = models.CharField(max_length=50, blank=True, null=True)
# 	reorder_level = models.IntegerField(default='0', blank=True, null=True)
# 	last_updated = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
# 	timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)


# from django.db import models
# from inventory_management.models import Inventory_Stock
# from accounts.models import CustomUser



# from django.db import models
# from inventory_management.models import Inventory_Stock
# from accounts.models import CustomUser

# class IssueItem(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
#     item = models.ForeignKey(Inventory_Stock, on_delete=models.CASCADE, blank=True, null=True)
#     issue_quantity = models.IntegerField(default=0, blank=True, null=True)
#     issue_by = models.CharField(max_length=50, blank=True, null=True)
#     issue_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
#     issue_date = models.DateField(blank=True, null=True)
#     issue_time = models.TimeField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.item.item_name} ({self.issue_quantity})"

   


   