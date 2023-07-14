from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SportsItemsRequestForm
from .models import SportsItemRequest


@login_required(login_url='login')
def create_sports_item_request(request):
    if request.method == 'POST':
        form = SportsItemsRequestForm(request.POST)
        if form.is_valid():
            sports_item_request = form.save(commit=False)
            sports_item_request.user = request.user
            sports_item_request.save()
            # Redirect to a success page or perform any other desired action
            return redirect('sports_items_req:create_sports_item_request')
    else:
        form = SportsItemsRequestForm()

    return render(request, 'create_sports_item_request.html', {'form': form})


from django.shortcuts import render
from .models import SportsItemRequest

def sports_item_requests_view(request):
    user = request.user
    requests = SportsItemRequest.objects.filter(user=user).select_related('category', 'item')
    return render(request, 'sports_item_requests.html', {'requests': requests})


from django.shortcuts import render

from django.shortcuts import render
from .models import SportsItemRequest


from django.shortcuts import render
from .models import SportsItemRequest

def list_requests_view(request):
    user = request.user
    first_name = user.first_name  # Retrieve user's first name from CustomUser model
    requests = SportsItemRequest.objects.filter(user=user)
    context = {
        "first_name": first_name,
        "requests": requests
    }
    return render(request, 'list_requests.html', context)



from django.shortcuts import render, get_object_or_404, redirect
from .models import SportsItemRequest
from .forms import SportsItemsRequestForm,SportsItemRequestUpdateForm
from django.contrib import messages

def update_sports_item_request(request, pk):
    queryset = SportsItemRequest.objects.get(request_id=pk)
    form = SportsItemRequestUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = SportsItemRequestUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Item updated successfully')
            return redirect('sports_items_req:list_requests')

    context = {
        'form': form
    }
    return render(request, 'update_sports_item_request.html', context)

