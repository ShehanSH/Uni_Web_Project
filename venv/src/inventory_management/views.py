from django.shortcuts import render, redirect
from .models import *
from .forms import InventoryCreateForm
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
    title = "sports_items"
    queryset = Inventory_Stock.objects.all()
    context = {
        "title": title,
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
