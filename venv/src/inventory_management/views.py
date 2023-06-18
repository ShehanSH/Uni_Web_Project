from django.shortcuts import render, redirect
from .models import *
from .forms import InventoryCreateForm, InventorySearchForm
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
        queryset = Inventory_Stock.objects.filter(category__icontains=form['category'].value(),
                                                  item_name__icontains=form['item_name'].value()
                                                  )
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

