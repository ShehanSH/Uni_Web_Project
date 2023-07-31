from django.shortcuts import render, redirect
# from .models import *
# from django.contrib import messages
# from .forms import InventoryCreateForm, InventorySearchForm, InventoryUpdateForm
# from django.http import HttpResponse
# import csv
# from .forms import *
# from django.contrib.auth.decorators import login_required
# # Create your views here.
from django.contrib.auth import logout
# from django.shortcuts import redirect
# def home(request):
#     title = "Welcome: This is the Home Page"
#     form = "This is home page body"
#     context = {
#         "title": title,
#         "form": form,
#     }
#     return render(request, 'home.html', context)

#locked user account
def account_lockout_view(request):
    return render(request, 'lockout.html')


def homemain(request):
  
    context = {
        
    }
    return render(request, 'homemain.html', context)

def slidebar(request):
  
    context = {
        
    }
    return render(request, 'slidebar.html', context)

def testchart(request):
    categories = Category.objects.all()
    selected_category_id = request.GET.get('category')  # Get the selected category ID from the request
    
    if selected_category_id:
        inventorys = Inventory_Stock.objects.filter(category_id=selected_category_id)
    else:
        inventorys = Inventory_Stock.objects.all()

    context = {
        "inventorys": inventorys,
        "categories": categories,
        "selected_category_id": int(selected_category_id) if selected_category_id else None,
    }
    return render(request, 'testchart.html', context)


def test2(request):
  
    context = {
        
    }
    return render(request, 'test2.html', context)

# def test(request):
#     title = "Welcome: This is the test Page"
   
#     context = {
#         "title": title,
#     }
#     return render(request, 'test.html', context)


# def list_items(request):
    
#     form = InventorySearchForm(request.POST or None)
#     queryset = Inventory_Stock.objects.all()
#     context = {
      
#         "queryset": queryset,
#         "form": form,
#     }

#     # if request.method == 'POST':
#     #     queryset = Inventory_Stock.objects.filter(
#     #         # category__icontains=form['category'].value(),
#     #         # category__name__icontains=form['category'].value(),
#     #         item_name__icontains=form['item_name'].value()
#     #     )

#     if request.method == 'POST':
#         category = form['category'].value()
#         queryset = Inventory_Stock.objects.filter(
#             item_name__icontains=form['item_name'].value()
#         )

#         if category != '':
#             queryset = queryset.filter(category_id=category)


#         if form['export_to_CSV'].value() == True:
#             response = HttpResponse(content_type='text/csv')
#             response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
#             writer = csv.writer(response)
#             writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
#             instance = queryset
#             for stock in instance:
#                 writer.writerow([stock.category, stock.item_name, stock.quantity])
#             return response

#         context = {
#             "form": form,
#             "header": header,
#             "queryset": queryset,
#         }
    
#     return render(request, 'list_items.html', context)


# def add_items(request):
#     form = InventoryCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         messages.success(request, 'Item added successfully')
#         return redirect('/list_items')
    
#     context = {
#         "form": form,
#         "title": "Add Item",
#     }
#     return render(request, 'add_items.html', context)


# def update_items(request, pk):
#     queryset = Inventory_Stock.objects.get(id=pk)
#     form = InventoryUpdateForm(instance=queryset)
#     if request.method == 'POST':
#         form = InventoryUpdateForm(request.POST, instance=queryset)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Item updated successfully')
#             return redirect('/list_items')

#     context = {
#         'form': form
#     }
#     return render(request, 'add_items.html', context)


# def delete_items(request, pk):
#     queryset = Inventory_Stock.objects.get(id=pk)
#     if request.method == 'POST':
#         queryset.delete()
#         messages.success(request, 'Item deleted successfully')
#         return redirect('/list_items')
#     return render(request, 'delete_items.html')


# def stock_detail(request, pk):
# 	queryset = Inventory_Stock.objects.get(id=pk)
# 	context = {
#         "title": queryset.item_name,
# 		"queryset": queryset,
# 	}
# 	return render(request, "stock_detail.html", context)


# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Inventory_Stock
# from .forms import IssueForm

# def issue_items(request, pk):
# 	queryset =Inventory_Stock.objects.get(id=pk)
# 	form = IssueForm(request.POST or None, instance=queryset)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.quantity -= instance.issue_quantity
# 		instance.issue_by = str(request.user)
# 		messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
# 		instance.save()

# 		return redirect('/stock_detail/'+str(instance.id))
# 		# return HttpResponseRedirect(instance.get_absolute_url())

# 	context = {
# 		"title": 'Issue ' + str(queryset.item_name),
# 		"queryset": queryset,
# 		"form": form,
# 		"username": 'Issue By: ' + str(request.user),
# 	}
# 	return render(request, "add_items.html", context)



# def receive_items(request, pk):
# 	queryset = Inventory_Stock.objects.get(id=pk)
# 	form = ReceiveForm(request.POST or None, instance=queryset)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.quantity += instance.receive_quantity
# 		instance.save()
# 		messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name)+"s now in Store")

# 		return redirect('/stock_detail/'+str(instance.id))
# 		# return HttpResponseRedirect(instance.get_absolute_url())
# 	context = {
# 			"title": 'Reaceive ' + str(queryset.item_name),
# 			"instance": queryset,
# 			"form": form,
# 			"username": 'Receive By: ' + str(request.user),
# 		}
# 	return render(request, "add_items.html", context)



# def reorder_level(request, pk):
# 	queryset = Inventory_Stock.objects.get(id=pk)
# 	form = ReorderLevelForm(request.POST or None, instance=queryset)
# 	if form.is_valid():
# 		item = form.save(commit=False)
# 		item.save()
# 		messages.success(request, "Reorder level for " + str(item.item_name) + " is updated to " + str(item.reorder_level))

# 		return redirect("/list_items")
# 	context = {
# 			"instance": queryset,
# 			"form": form,
# 		}
# 	return render(request, "add_items.html", context)


# def list_history(request):
#     header = 'LIST OF ITEMS'
#     queryset = Inventory_Stock_History.objects.all()
#     form = InventoryStockHistorySearchForm(request.POST or None)
#     context = {
#         "header": header,
#         "queryset": queryset,
#         "form": form,
#     }

#     if request.method == 'POST':
#         category = form['category'].value()
#         queryset = Inventory_Stock_History.objects.filter(
#             item_name__icontains=form['item_name'].value(),
#             last_updated__range=[
#                                     form['start_date'].value(),
#                                     form['end_date'].value()
#                                 ]
#         )

#         if category != '':
#             queryset = queryset.filter(category_id=category)

#         if form['export_to_CSV'].value() == True:
#                 response = HttpResponse(content_type='text/csv')
#                 response['Content-Disposition'] = 'attachment; filename="Stock History.csv"'
#                 writer = csv.writer(response)
#                 writer.writerow(
#                     ['CATEGORY',
#                      'ITEM NAME',
#                      'QUANTITY',
#                      'ISSUE QUANTITY',
#                      'RECEIVE QUANTITY',
#                      'RECEIVE BY',
#                      'ISSUE BY',
#                      'LAST UPDATED'])
#                 instance = queryset
#                 for stock in instance:
#                     writer.writerow(
#                         [stock.category,
#                          stock.item_name,
#                          stock.quantity,
#                          stock.issue_quantity,
#                          stock.receive_quantity,
#                          stock.receive_by,
#                          stock.issue_by,
#                          stock.last_updated])
#                 return response

#         context = {
#             "form": form,
#             "header": header,
#             "queryset": queryset,
#         }

#     return render(request, "list_history.html", context)

# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render

# @login_required(login_url='login')
# def index(request):
#     # Get the current user ID and role name
#     user_id = request.user.user_id
#     role_name = request.user.role.role_name

#     context = {'user_id': user_id, 'role_name': role_name}
#     return render(request, 'index.html', context)




def logout_view(request):
    logout(request)
    return redirect('/')  # Replace 'home' with the desired URL after logout

# from django.shortcuts import render, redirect
# from .forms import Inventory_Stock_CreateForm, AddSupplierForm

# def create_inventory_stock(request):
#     if request.method == 'POST':
#         form = Inventory_Stock_CreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_url')  # Redirect to a success page after saving the inventory stock.
#     else:
#         form = Inventory_Stock_CreateForm()

#     return render(request, 'create_inventory_stock.html', {'form': form})

# def add_supplier(request):
#     if request.method == 'POST':
#         form = AddSupplierForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_url')  # Redirect to a success page after saving the supplier.
#     else:
#         form = AddSupplierForm()

#     return render(request, 'add_supplier.html', {'form': form})

from .models import Category, Supplier, Inventory_Stock, Supply_Inventory
from .forms import InventoryStockForm


def inventory_chart(request):
    inventorys = Inventory_Stock.objects.all()
    context = {
        "inventorys": inventorys,
       
    }

    return render(request, 'inventoryChart.html', context)



# views.py
from django.shortcuts import render
from .models import Inventory_Stock
# views.py
from django.shortcuts import render
from .models import Inventory_Stock
from .forms import CategoryFilterForm,InventoryReorderFilterForm

#CHART 1 stock quantity, damage quantity, lost quantity vs item name
def inventory_chart_view(request):
    # Retrieve data from the model
    queryset = Inventory_Stock.objects.all()

    # Handle category filter using the form
    form = CategoryFilterForm(request.GET)
    if form.is_valid():
        category = form.cleaned_data.get('categories')
        if category:
            queryset = queryset.filter(category=category)

    # Prepare data for the Plotly bar chart
    item_names = [item.item_name for item in queryset]
    stock_quantity = [item.stock_quantity for item in queryset]
    damage_quantity = [item.damage_quantity for item in queryset]
    lost_quantity = [item.lost_quantity for item in queryset]

    # Prepare data for the Plotly bar chart - Reorder level
    reorder_level = [item.reorder_level for item in queryset]

    # Pass data and form to the template
    context = {
        'item_names': item_names,
        'stock_quantity': stock_quantity,
        'damage_quantity': damage_quantity,
        'lost_quantity': lost_quantity,
        'reorder_level': reorder_level,
        'form': form,
    }

    return render(request, 'inventory_chart_view.html', context)


#CHART 2 stock quantity, reorder level vs item name
def inventory_reorder_chart_view(request):
    # Retrieve data from the model
    queryset = Inventory_Stock.objects.all()

    # Handle category filter using the form
    form = InventoryReorderFilterForm(request.GET)
    if form.is_valid():
        category = form.cleaned_data.get('categories')
        if category:
            queryset = queryset.filter(category=category)

    # Prepare data for the Plotly bar chart
    item_names = [item.item_name for item in queryset]
    stock_quantity = [item.stock_quantity for item in queryset]
    # Prepare data for the Plotly bar chart - Reorder level
    reorder_level = [item.reorder_level for item in queryset]

    # Pass data and form to the template
    context = {
        'item_names': item_names,
        'stock_quantity': stock_quantity,
      
        'reorder_level': reorder_level,
        'form': form,
    }

    return render(request, 'inventory_reorder_chart_view.html', context)

from django.shortcuts import render
from .models import Category, Inventory_Stock
from .forms import InventoryStockCountFilterForm
from django.db import models

#CHART 3 stock quantity vs item name with category
# views.py
import plotly.graph_objs as go
from django.shortcuts import render
from .forms import CategoryForm
from .models import Inventory_Stock

from django.shortcuts import render
from .forms import InventoryStockCountFilterForm
from .models import Inventory_Stock

def inventory_stock_count_chart_view(request):
    form = InventoryStockCountFilterForm(request.GET)
    stock_items = Inventory_Stock.objects.all()

    # Apply category filter if selected
    if form.is_valid() and form.cleaned_data['categories']:
        stock_items = stock_items.filter(category=form.cleaned_data['categories'])

    total_stock_quantity = sum(item.stock_quantity for item in stock_items)
    
    category_names = [item.item_name for item in stock_items]
    stock_percentages = [(item.stock_quantity / total_stock_quantity) * 100 for item in stock_items]

    context = {
        'form': form,
        'category_names': category_names,
        'stock_percentages': stock_percentages,
    }
    return render(request, 'inventory_stock_count_chart_view.html', context)



#supplier CHART 
# views.py
import plotly.graph_objs as go
from django.shortcuts import render
from .forms import SupplierChartFilterForm
from .models import Supply_Inventory
from django.db.models import Sum

import plotly.graph_objs as go
from django.shortcuts import render
from django.db.models import Sum  # Import Sum to perform aggregation
from .forms import SupplierChartFilterForm
from .models import Supply_Inventory

def supplier_chart_view(request):
    # Retrieve data from the model
    queryset = Supply_Inventory.objects.all()

    # Handle category and date range filters using the form
    form = SupplierChartFilterForm(request.GET)
    if form.is_valid():
      
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')

    
        if start_date:
            queryset = queryset.filter(supply_date__gte=start_date)
        if end_date:
            queryset = queryset.filter(supply_date__lte=end_date)

    # Calculate the total supply_quantity for each category
    category_totals = (
        queryset.values('category__name')  # Use 'category__name' instead of 'category_name'
        .annotate(total_supply=Sum('supply_quantity'))
    )

    # Prepare data for the Plotly pie chart
    item_names = [item['category__name'] for item in category_totals]
    supply_quantity = [item['total_supply'] for item in category_totals]

    # Calculate the percentage for each category
    total_supply_quantity = sum(supply_quantity)
    supply_percentages = [(qty / total_supply_quantity) * 100 for qty in supply_quantity]

    # Pass data and form to the template
    context = {
        'item_names': item_names,
        'supply_percentages': supply_percentages,
        'form': form,
    }

    return render(request, 'supplier_chart_view.html', context)

#supplier CHART 2

# views.py
# views.py
import plotly.graph_objs as go
from django.shortcuts import render
from django.db.models import Sum
from .forms import SupplierNameChartFilterForm
from .models import Supply_Inventory

# views.py
import plotly.graph_objs as go
from django.shortcuts import render
from django.db.models import Sum
from .forms import SupplierNameChartFilterForm
from .models import Supplier, Supply_Inventory

# views.py
import plotly.graph_objs as go
from django.shortcuts import render
from django.db.models import Sum
from .forms import SupplierNameChartFilterForm
from .models import Supplier, Supply_Inventory

def supplier_name_chart(request):
    # Retrieve data from the model
    queryset = Supply_Inventory.objects.all()

    # Handle supplier, start date, and end date filters using the form
    form = SupplierNameChartFilterForm(request.GET)
    if form.is_valid():
        supplier = form.cleaned_data.get('suppliers')
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')

        if supplier:
            queryset = queryset.filter(Supplier=supplier)
        if start_date:
            queryset = queryset.filter(supply_date__gte=start_date)
        if end_date:
            queryset = queryset.filter(supply_date__lte=end_date)

    # Calculate the total supply_quantity for each supplier
    supplier_totals = (
        queryset.values('Supplier__supplier_name')
        .annotate(total_supply=Sum('supply_quantity'))
    )

    # Prepare data for the Plotly bar chart
    supplier_names = [item['Supplier__supplier_name'] for item in supplier_totals]
    supply_quantity = [item['total_supply'] for item in supplier_totals]

    # Pass data and form to the template
    context = {
        'supplier_names': supplier_names,
        'supply_quantity': supply_quantity,
        'form': form,
    }

    return render(request, 'supplier_name_chart.html', context)


#CHART 3

# views.py
import plotly.graph_objs as go
from django.shortcuts import render
from django.db.models import Sum
from .forms import SupplierNameChartFilterForm
from .models import Supply_Inventory

from django.shortcuts import render
from django.db.models import Sum
from .models import Supply_Inventory
from .forms import InventoryStockOverTimeFilterForm
import json

# views.py
def supply_inventory_stock_over_time(request):
    # Retrieve data from the model
    queryset = Supply_Inventory.objects.all()

    # Handle item, category, start date, and end date filters using the form
    form = InventoryStockOverTimeFilterForm(request.GET)
    if form.is_valid():
        item = form.cleaned_data.get('items')
        category = form.cleaned_data.get('category')
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')

        if item:
            queryset = queryset.filter(item=item)
        if category:
            queryset = queryset.filter(category=category)
        if start_date:
            queryset = queryset.filter(supply_date__gte=start_date)
        if end_date:
            queryset = queryset.filter(supply_date__lte=end_date)

    # Calculate the total supply_quantity for each date
    date_totals = (
        queryset.values('supply_date')
        .annotate(total_supply=Sum('supply_quantity'))
    )

    # Prepare data for the Plotly line chart
    supply_dates = [item['supply_date'].strftime('%Y-%m-%d') for item in date_totals]
    total_supply_quantity = [item['total_supply'] for item in date_totals]

    # Pass data and form to the template
    context = {
        'supply_dates': supply_dates,
        'total_supply_quantity': total_supply_quantity,
        'form': form,
    }

    return render(request, 'supply_inventory_stock_over_time.html', context)




#REPORTING

# views.py
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Inventory_Stock
from .tables import InventoryStockTable
from django.http import HttpResponse
import csv
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.files.storage import default_storage
from reportlab.pdfgen import canvas



from django.http import HttpResponse
from django.shortcuts import render
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet
import csv



#htmltopdf

# views.py

import csv
from django.shortcuts import render, HttpResponse
from .models import Inventory_Stock
from .pdf import render_to_pdf
from django.contrib.staticfiles import finders
from django.templatetags.static import static
#report 1
def generate_pdf(request):
    items = Inventory_Stock.objects.all()

    context = {
        'items': items,
    }

    pdf = render_to_pdf('inventory_stock_pdf.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'filename=inventory_stock.pdf'
        return response

    return HttpResponse("Failed to generate PDF.")

def generate_csv(request):
    items = Inventory_Stock.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inventory_stock.csv"'

    writer = csv.writer(response)
    writer.writerow(['Category', 'Item Name', 'Stock Quantity', 'Reorder Quantity'])
    for item in items:
        writer.writerow([item.category, item.item_name, item.stock_quantity, item.reorder_level])

    return response

# views.py
from django.shortcuts import render
from .models import Inventory_Stock, Category


def reorder_report(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        selected_categories = request.POST.getlist('selected_categories')
        if 'all_categories' in request.POST:
            selected_categories = [category.category_id for category in categories]
        file_type = request.POST.get('generate')

        if file_type == 'pdf':
            items = Inventory_Stock.objects.filter(category__in=selected_categories)
            context = {
                'items': items,
            }

            # Calculate the "Refill Quantity" for each item in the view
            for item in items:
                item.refill_quantity = item.reorder_level - item.stock_quantity
                item.display_refill_quantity = item.refill_quantity if item.refill_quantity > 0 else "No need to refill"

            pdf = render_to_pdf('inventory_stock_pdf.html', context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] = 'filename=inventory_stock.pdf'
                return response

        elif file_type == 'csv':
            return generate_csv(request)

    context = {
        'categories': categories,
    }
    return render(request, 'inventory_report.html', context)

#report 2


# # views.py
# import csv
# from django.shortcuts import render, HttpResponse
# from .models import Inventory_Stock, Category

# def generate_pdf2(request):
#     categories = Category.objects.annotate(
#         total_stock_quantity=models.Sum('inventory_stock__stock_quantity'),
#         total_damage_quantity=models.Sum('inventory_stock__damage_quantity'),
#         total_lost_quantity=models.Sum('inventory_stock__lost_quantity')
#     )

#     context = {
#         'categories': categories,
#     }

#     pdf = render_to_pdf('inventory_stock_pdf_2.html', context)
#     if pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         response['Content-Disposition'] = 'filename=category_inventory_report.pdf'
#         return response

#     return HttpResponse("Failed to generate PDF.")


# def generate_pdf2(request):
#     items = Inventory_Stock.objects.all()

#     context = {
#         'items': items,
#     }

#     pdf = render_to_pdf('inventory_stock_pdf_2.html', context)
#     if pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         response['Content-Disposition'] = 'filename=category_inventory_report.pdf'
#         return response

#     return HttpResponse("Failed to generate PDF.")


# def generate_csv2(request):
#     items = Inventory_Stock.objects.all()

#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="category_inventory_report.csv"'

#     writer = csv.writer(response)
#     writer.writerow(['Category', 'Item Name', 'Stock Quantity', 'Damage Quantity', 'Lost Quantity'])
#     for item in items:
#         writer.writerow([item.category.name, item.item_name, item.stock_quantity, item.damage_quantity, item.lost_quantity])

#     return response



# def select_file_type2(request):
#     if request.method == 'POST':
#         file_type = request.POST.get('file_type')

#         if file_type == 'pdf':
#             return generate_pdf2(request)

#         elif file_type == 'csv':
#             return generate_csv2(request)

#     categories = Category.objects.annotate(
#         total_stock_quantity=models.Sum('inventory_stock__stock_quantity'),
#         total_damage_quantity=models.Sum('inventory_stock__damage_quantity'),
#         total_lost_quantity=models.Sum('inventory_stock__lost_quantity')
#     )

#     context = {
#         'categories': categories,
#     }
#     return render(request, 'select_file_type.html', context)

# def reorder_report2(request):
#     categories = Category.objects.all()

#     if request.method == 'POST':
#         selected_categories = request.POST.getlist('selected_categories')
#         if 'all_categories' in request.POST:
#             selected_categories = [category.category_id for category in categories]
#         file_type = request.POST.get('generate')

#         if file_type == 'pdf':
#             items = Inventory_Stock.objects.filter(category__in=selected_categories)
#             context = {
#                 'items': items,
#             }
#             pdf = render_to_pdf('inventory_stock_pdf_2.html', context)
#             if pdf:
#                 response = HttpResponse(pdf, content_type='application/pdf')
#                 response['Content-Disposition'] = 'filename=inventory_stock.pdf'
#                 return response

#         elif file_type == 'csv':
#             return generate_csv(request)

#     context = {
#         'categories': categories,
#     }
#     return render(request, 'inventory_stock_pdf_2.html', context)


# def generate_pdf2(request):
#     selected_categories = request.POST.getlist('selected_categories')  # Get selected categories from the form
#     items = Inventory_Stock.objects.filter(category__category_id__in=selected_categories)

#     context = {
#         'items': items,
#     }

#     pdf = render_to_pdf('inventory_stock_pdf_2.html', context)
#     if pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         response['Content-Disposition'] = 'filename=category_inventory_report.pdf'
#         return response

#     return HttpResponse("Failed to generate PDF.")

# def generate_csv2(request):
#     selected_categories = request.POST.getlist('selected_categories')  # Get selected categories from the form
#     items = Inventory_Stock.objects.filter(category__category_id__in=selected_categories)

#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="category_inventory_report.csv"'

#     writer = csv.writer(response)
#     writer.writerow(['Category', 'Item Name', 'Stock Quantity', 'Damage Quantity', 'Lost Quantity'])
#     for item in items:
#         writer.writerow([item.category.name, item.item_name, item.stock_quantity, item.damage_quantity, item.lost_quantity])

#     return response

# def select_file_type2(request):
#     categories = Category.objects.annotate(
#         total_stock_quantity=models.Sum('inventory_stock__stock_quantity'),
#         total_damage_quantity=models.Sum('inventory_stock__damage_quantity'),
#         total_lost_quantity=models.Sum('inventory_stock__lost_quantity')
#     )

#     if request.method == 'POST':
#         file_type = request.POST.get('file_type')

#         if file_type == 'pdf':
#             return generate_pdf2(request)

#         elif file_type == 'csv':
#             return generate_csv2(request)

#     context = {
#         'categories': categories,
#     }
#     return render(request, 'select_file_type.html', context)



# views2.py
import csv
from django.shortcuts import render, HttpResponse
from .models import Inventory_Stock
from .pdf import render_to_pdf
from django.contrib.staticfiles import finders
from django.templatetags.static import static

# report 1
def generate_pdf2(request):
    items = Inventory_Stock.objects.all()

    context = {
        'items': items,
    }

    pdf = render_to_pdf('inventory_stock_pdf2.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'filename=inventory_stock.pdf'
        return response

    return HttpResponse("Failed to generate PDF.")

def generate_csv2(request):
    items = Inventory_Stock.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inventory_stock.csv"'

    writer = csv.writer(response)
    writer.writerow(['Category', 'Item Name', 'Stock Quantity', 'Reorder Quantity'])
    for item in items:
        writer.writerow([item.category, item.item_name, item.stock_quantity, item.reorder_level])

    return response

# Rename reorder_report function to reorder_report2
def reorder_report2(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        selected_categories = request.POST.getlist('selected_categories')
        if 'all_categories' in request.POST:
            selected_categories = [category.category_id for category in categories]
        file_type = request.POST.get('generate')

        if file_type == 'pdf':
            items = Inventory_Stock.objects.filter(category__in=selected_categories)
            total_stock = items.aggregate(Sum('stock_quantity'))['stock_quantity__sum']
            total_damage = items.aggregate(Sum('damage_quantity'))['damage_quantity__sum']
            total_lost = items.aggregate(Sum('lost_quantity'))['lost_quantity__sum']

            context = {
                'items': items,
                'total_stock': total_stock,
                'total_damage': total_damage,
                'total_lost': total_lost,
            }

            pdf = render_to_pdf('inventory_stock_pdf2.html', context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] = 'filename=inventory_stock.pdf'
                return response

        elif file_type == 'csv':
            return generate_csv2(request)

    context = {
        'categories': categories,
    }
    return render(request, 'inventory_report2.html', context)
#supply reports
#reports 1

# views3.py
# views3.py
import csv
from django.shortcuts import render, HttpResponse
from .models import Supply_Inventory
from .pdf import render_to_pdf
from django.contrib.staticfiles import finders
from django.templatetags.static import static

# views3.py
import csv
from django.shortcuts import render, HttpResponse
from .models import Supply_Inventory
from .pdf import render_to_pdf
from django.contrib.staticfiles import finders
from django.templatetags.static import static

# views3.py
import csv
from django.shortcuts import render, HttpResponse
from .models import Supply_Inventory
from .pdf import render_to_pdf
from django.contrib.staticfiles import finders
from django.templatetags.static import static

# views3.py
# views3.py
from django.shortcuts import render, HttpResponse
from .models import Supply_Inventory
from .pdf import render_to_pdf
import csv

def generate_pdf3(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if not start_date or not end_date:
            return HttpResponse("Please select both start date and end date.")

        items = Supply_Inventory.objects.filter(supply_date__range=(start_date, end_date))

        context = {
            'items': items,
            'start_date': start_date,
            'end_date': end_date,
        }

        pdf = render_to_pdf('supply_stock_pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'filename=supply_stock_{start_date}_to_{end_date}.pdf'
            return response

    return render(request, 'supply_stock.html')

def generate_csv3(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if not start_date or not end_date:
            return HttpResponse("Please select both start date and end date.")

        items = Supply_Inventory.objects.filter(supply_date__range=(start_date, end_date))

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="supply_stock_{start_date}_to_{end_date}.csv"'

        writer = csv.writer(response)
        writer.writerow(['Supply Date', 'Supply Time', 'Supplier', 'Item Supplied', 'Category', 'Quantity Supplied'])
        for item in items:
            writer.writerow([item.supply_date, item.supply_time, item.Supplier.supplier_name, item.item.item_name, item.category.name, item.supply_quantity])

        return response

    return render(request, 'supply_stock.html')

from django.db.models import Sum

def reorder_report3(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        generate_format = request.POST.get('generate')
        selected_suppliers = request.POST.getlist('selected_suppliers')  # List of selected supplier IDs

        if start_date and end_date:
            items = Supply_Inventory.objects.filter(supply_date__range=(start_date, end_date))

            # Filter items by selected suppliers if any are chosen
            if 'all' not in selected_suppliers and selected_suppliers:
                items = items.filter(Supplier__id__in=selected_suppliers)
        else:
            items = []

        total_supply_count = items.aggregate(Sum('supply_quantity'))['supply_quantity__sum']

        context = {
            'items': items,
            'start_date': start_date,
            'end_date': end_date,
            'suppliers': Supplier.objects.all(),  # Add this to pass all suppliers to the template
            'total_supply_count': total_supply_count,
        }

        if generate_format == 'pdf':
            pdf = render_to_pdf('supply_stock_pdf.html', context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] = f'filename=supply_stock_{start_date}_to_{end_date}.pdf'
                return response
        elif generate_format == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="supply_stock_{start_date}_to_{end_date}.csv"'

            writer = csv.writer(response)
            writer.writerow(['Supply Date', 'Supply Time', 'Supplier', 'Item Supplied', 'Category', 'Quantity Supplied'])
            for item in items:
                writer.writerow([item.supply_date, item.supply_time, item.Supplier.supplier_name, item.item.item_name, item.category.name, item.supply_quantity])

            return response

    context = {
        'suppliers': Supplier.objects.all(),
    }
    return render(request, 'supply_stock.html', context)


