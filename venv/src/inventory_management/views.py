from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import InventoryCreateForm, InventorySearchForm, InventoryUpdateForm
from django.http import HttpResponse
import csv
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import logout
from django.shortcuts import redirect
def home(request):
    title = "Welcome: This is the Home Page"
    form = "This is home page body"
    context = {
        "title": title,
        "form": form,
    }
    return render(request, 'home.html', context)


def homemain(request):
  
    context = {
        
    }
    return render(request, 'homemain.html', context)



def test(request):
    title = "Welcome: This is the test Page"
   
    context = {
        "title": title,
    }
    return render(request, 'test.html', context)


def list_items(request):
    
    form = InventorySearchForm(request.POST or None)
    queryset = Inventory_Stock.objects.all()
    context = {
      
        "queryset": queryset,
        "form": form,
    }

    # if request.method == 'POST':
    #     queryset = Inventory_Stock.objects.filter(
    #         # category__icontains=form['category'].value(),
    #         # category__name__icontains=form['category'].value(),
    #         item_name__icontains=form['item_name'].value()
    #     )

    if request.method == 'POST':
        category = form['category'].value()
        queryset = Inventory_Stock.objects.filter(
            item_name__icontains=form['item_name'].value()
        )

        if category != '':
            queryset = queryset.filter(category_id=category)


        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.category, stock.item_name, stock.quantity])
            return response

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }
    
    return render(request, 'list_items.html', context)


def add_items(request):
    form = InventoryCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Item added successfully')
        return redirect('/list_items')
    
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, 'add_items.html', context)


def update_items(request, pk):
    queryset = Inventory_Stock.objects.get(item_id=pk)
    form = InventoryUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = InventoryUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully')
            return redirect('/list_items')

    context = {
        'form': form
    }
    return render(request, 'add_items.html', context)


def delete_items(request, pk):
    queryset = Inventory_Stock.objects.get(item_id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Item deleted successfully')
        return redirect('/list_items')
    return render(request, 'delete_items.html')


def stock_detail(request, pk):
	queryset = Inventory_Stock.objects.get(item_id=pk)
	context = {
        "title": queryset.item_name,
		"queryset": queryset,
	}
	return render(request, "stock_detail.html", context)


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Inventory_Stock
from .forms import IssueForm

def issue_items(request, pk):
    queryset = Inventory_Stock.objects.get(item_id=pk)
    form = IssueForm(request.POST or None, instance=queryset)

    if form.is_valid():
        issue_quantity = form.cleaned_data['issue_quantity']

        if issue_quantity > queryset.quantity:
            messages.error(request, f"Cannot issue sports item. Stock has only {queryset.quantity} {queryset.item_name}s available.")
        else:
            instance = form.save(commit=False)
            instance.receive_quantity = 0
            instance.quantity -= issue_quantity
            instance.issue_by = str(request.user)
            instance.save()
            messages.success(request, f"Issued {issue_quantity} {instance.item_name}s SUCCESSFULLY. {instance.quantity} {instance.item_name}s now left in Store")
            return redirect('/stock_detail/' + str(instance.item_id))

    context = {
        "title": 'Issue ' + str(queryset.item_name),
        "queryset": queryset,
        "form": form,
        "username": 'Issue By: ' + str(request.user),
    }
    return render(request, "add_items.html", context)




def receive_items(request, pk):
    queryset = Inventory_Stock.objects.get(item_id=pk)
    form = ReceiveForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.issue_quantity = 0
        instance.quantity += instance.receive_quantity
        instance.receive_by = str(request.user)
        instance.save()
        messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name) + "s now in Store")

        return redirect('/stock_detail/' + str(instance.item_id))
        # return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": 'Receive ' + str(queryset.item_name),
        "instance": queryset,
        "form": form,
        "username": 'Receive By: ' + str(request.user),
    }
    return render(request, "add_items.html", context)



def reorder_level(request, pk):
	queryset = Inventory_Stock.objects.get(item_id=pk)
	form = ReorderLevelForm(request.POST or None, instance=queryset)
	if form.is_valid():
		item = form.save(commit=False)
		item.save()
		messages.success(request, "Reorder level for " + str(item.item_name) + " is updated to " + str(item.reorder_level))

		return redirect("/list_items")
	context = {
			"instance": queryset,
			"form": form,
		}
	return render(request, "add_items.html", context)


def list_history(request):
    header = 'LIST OF ITEMS'
    queryset = Inventory_Stock_History.objects.all()
    form = InventoryStockHistorySearchForm(request.POST or None)
    context = {
        "header": header,
        "queryset": queryset,
        "form": form,
    }

    if request.method == 'POST':
        category = form['category'].value()
        queryset = Inventory_Stock_History.objects.filter(
            item_name__icontains=form['item_name'].value(),
            last_updated__range=[
                                    form['start_date'].value(),
                                    form['end_date'].value()
                                ]
        )

        if category != '':
            queryset = queryset.filter(category_id=category)

        if form['export_to_CSV'].value() == True:
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="Stock History.csv"'
                writer = csv.writer(response)
                writer.writerow(
                    ['CATEGORY',
                     'ITEM NAME',
                     'QUANTITY',
                     'ISSUE QUANTITY',
                     'RECEIVE QUANTITY',
                     'RECEIVE BY',
                     'ISSUE BY',
                     'LAST UPDATED'])
                instance = queryset
                for stock in instance:
                    writer.writerow(
                        [stock.category,
                         stock.item_name,
                         stock.quantity,
                         stock.issue_quantity,
                         stock.receive_quantity,
                         stock.receive_by,
                         stock.issue_by,
                         stock.last_updated])
                return response

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }

    return render(request, "list_history.html", context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def index(request):
    # Get the current user ID and role name
    user_id = request.user.user_id
    role_name = request.user.role.role_name

    context = {'user_id': user_id, 'role_name': role_name}
    return render(request, 'index.html', context)




def logout_view(request):
    logout(request)
    return redirect('/')  # Replace 'home' with the desired URL after logout
