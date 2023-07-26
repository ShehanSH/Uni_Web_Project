from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SportsItemsRequestForm, SportsItemRequestUpdateForm
from .models import SportsItemRequest
from django.contrib import messages

@login_required(login_url='login')
def create_sports_item_request(request):
    if request.method == 'POST':
        form = SportsItemsRequestForm(request.POST)
        if form.is_valid():
            sports_item_request = form.save(commit=False)
            sports_item_request.user = request.user
            sports_item_request.save()
            messages.success(request, 'Sports item request submitted successfully.')
            return redirect('sports_items_req:create_sports_item_request')
        else:
            messages.error(request, 'Error submitting the sports item request. Please check the form and try again.')
    else:
        form = SportsItemsRequestForm()

    return render(request, 'create_sports_item_request.html', {'form': form})

def sports_item_requests_view(request):
    user = request.user
    requests = SportsItemRequest.objects.filter(user=user).select_related('category', 'item')
    return render(request, 'sports_item_requests.html', {'requests': requests})

def list_requests_view(request):
    user = request.user
    first_name = user.first_name  # Retrieve user's first name from CustomUser model
    requests = SportsItemRequest.objects.filter(user=user)
    context = {
        "first_name": first_name,
        "requests": requests
    }
    return render(request, 'list_requests.html', context)

def update_sports_item_request(request, pk):
    queryset = get_object_or_404(SportsItemRequest, request_id=pk)
    form = SportsItemRequestUpdateForm(instance=queryset)

    if request.method == 'POST':
        form = SportsItemRequestUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sports item request updated successfully.')
            return redirect('sports_items_req:list_requests')
        else:
            messages.error(request, 'Error updating the sports item request. Please check the form and try again.')

    context = {
        'form': form
    }
    return render(request, 'update_sports_item_request.html', context)

def delete_request(request, pk):
    queryset = get_object_or_404(SportsItemRequest, request_id=pk)

    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Sports item request deleted successfully.')
        return redirect('sports_items_req:list_requests')

    return render(request, 'delete_request.html')