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



# views.py
from django.shortcuts import render
from .models import SportsItemRequest
from .forms import SportsItemReqStatusForm

# views.py
from django.shortcuts import render
from .models import SportsItemRequest
from .forms import SportsItemReqStatusForm
import plotly.graph_objects as go

def sports_item_req_status(request):
    form = SportsItemReqStatusForm(request.GET)

    # Filter data based on the form's input
    filtered_data = SportsItemRequest.objects.all()
    if form.is_valid():
        approval_status = form.cleaned_data.get('approval_status')
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        category = form.cleaned_data.get('category')

        if approval_status:
            filtered_data = filtered_data.filter(approval_status=approval_status)
        if start_date:
            filtered_data = filtered_data.filter(request_date__gte=start_date)
        if end_date:
            filtered_data = filtered_data.filter(request_date__lte=end_date)
        if category:
            filtered_data = filtered_data.filter(category=category)

    # Count requests in each approval status category
    approval_count = {
        'Approval': filtered_data.filter(approval_status='A').count(),
        'Disapproval': filtered_data.filter(approval_status='D').count(),
        'Issued': filtered_data.filter(approval_status='I').count(),
    }

    # Prepare data for the Plotly bar chart
    labels = list(approval_count.keys())
    data = list(approval_count.values())

    # Create the Plotly bar chart
    bar_chart = go.Figure(data=[go.Bar(x=labels, y=data)])

    # Convert the chart to HTML and pass it to the template
    chart_div = bar_chart.to_html(full_html=False)

    context = {
        'form': form,
        'chart_div': chart_div,
    }

    return render(request, 'sports_req_chart.html', context)

