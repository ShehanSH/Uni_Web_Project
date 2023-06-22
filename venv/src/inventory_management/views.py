from django.shortcuts import render, redirect
from .models import *
from .forms import InventoryCreateForm, InventorySearchForm, InventoryUpdateForm
from django.http import HttpResponse
import csv
# Create your views here.

def home(request):
    title = "Welcome: This is the Home Page"
    form = "This is home page body"
    context = {
        "title": title,
        "form": form,
    }
    return render(request, 'home.html', context)

def list_items(request):
    header = "Sports Items"
    form = InventorySearchForm(request.POST or None)
    queryset = Inventory_Stock.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "form": form,
    }

    if request.method == 'POST':
        queryset = Inventory_Stock.objects.filter(
            # category__icontains=form['category'].value(),
            item_name__icontains=form['item_name'].value()
        )

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
   if form.is_valid():      #validate form details
       form.save()
       return redirect('/list_items')
   context = {
        "form": form,
        "title": "Add Item",
    }
   return render(request, 'add_items.html', context)

def update_items(request, pk):
	queryset = Inventory_Stock.objects.get(id=pk)
	form = InventoryUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = InventoryUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/list_items')

	context = {
		'form':form
	}
	return render(request, 'add_items.html', context)


def delete_items(request, pk):
    queryset = Inventory_Stock.objects.get(id=pk) 
    if request.method == 'POST':
        queryset.delete()
        return redirect('/list_items')
    return render(request, 'delete_items.html')
