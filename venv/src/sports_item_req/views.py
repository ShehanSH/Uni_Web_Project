from django.shortcuts import render, redirect
from .forms import SportsItemReqForm
from .models import Category, Inventory_Stock

def create_sports_item_request(request):
    if request.method == 'POST':
        form = SportsItemReqForm(request.POST)
        if form.is_valid():
            try:
                # Dynamically populate item_name choices based on the selected category
                category_choices = Category.objects.all()
                item_choices = []
                category_id = request.POST.get('item_category')
                if category_id:
                    category = Category.objects.get(pk=category_id)
                    item_choices = [(item.item_id, item.item_name) for item in category.inventory_stock_set.all()]

                form.fields['item_category'].choices = [(category.category_id, category.name) for category in category_choices]
                form.fields['item_name'].choices = item_choices

                form.save()
                # Process the form submission or redirect to a success page
                return redirect('login')
            except Exception as e:
                # Log or print the error message for debugging
                print(f"An error occurred while saving the form: {str(e)}")
                # Handle the error as needed (e.g., show an error message to the user)
    else:
        form = SportsItemReqForm()
    
    return render(request, 'sports_items_request.html', {'form': form})
