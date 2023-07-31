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
import plotly.graph_objs as go
from django.shortcuts import render
from .models import SportsItemRequest
from django.db import models


from django.shortcuts import render
from .models import Inventory_Stock
from .forms import ItemRequestFilterForm
import plotly.graph_objs as go

def item_request_chart_view(request):
    # Retrieve data from the model
    queryset = SportsItemRequest.objects.all()

    # Handle filters using the form
    form = ItemRequestFilterForm(request.GET)
    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        category = form.cleaned_data.get('categories')

        if start_date:
            queryset = queryset.filter(request_date__gte=start_date)
        if end_date:
            queryset = queryset.filter(request_date__lte=end_date)
        if category:
            queryset = queryset.filter(category=category)

    # Prepare data for the Plotly bar chart
    approval_status_choices = dict(SportsItemRequest.APPROVAL_CHOICES)
    item_names = []
    request_quantity_approval = []
    request_quantity_disapproval = []
    request_quantity_issued = []

    for item in queryset:
        item_names.append(item.item.item_name)
        if item.approval_status == 'A':
            request_quantity_approval.append(item.req_quantity)
            request_quantity_disapproval.append(0)
            request_quantity_issued.append(0)
        elif item.approval_status == 'D':
            request_quantity_approval.append(0)
            request_quantity_disapproval.append(item.req_quantity)
            request_quantity_issued.append(0)
        elif item.approval_status == 'I':
            request_quantity_approval.append(0)
            request_quantity_disapproval.append(0)
            request_quantity_issued.append(item.req_quantity)

    # Create traces for each approval status
    trace_approval = go.Bar(x=item_names, y=request_quantity_approval, name='Approval', marker=dict(color='green'))
    trace_disapproval = go.Bar(x=item_names, y=request_quantity_disapproval, name='Disapproval', marker=dict(color='red'))
    trace_issued = go.Bar(x=item_names, y=request_quantity_issued, name='Issued', marker=dict(color='blue'))

    # Prepare the data for the chart
    data = [trace_approval, trace_disapproval, trace_issued]

    # Layout for the bar chart
    layout = go.Layout(
        title='Sports Item Requests by Approval Status',
        xaxis=dict(title='Item Names'),
        yaxis=dict(title='Request Quantity'),
        barmode='group'  # Use 'group' for grouped bars
    )

    # Render the bar chart
    chart = go.Figure(data=data, layout=layout)
    chart_div = chart.to_html(full_html=False)

    context = {
        'form': form,
        'chart_div': chart_div
    }

    return render(request, 'item_request_chart_view.html', context)


from django.shortcuts import render

from .models import SportsItemRequest
from datetime import datetime

# def sports_item_requests_trend_chart_view(request):
#     form = SportsItemRequestFilterForm(request.GET)
#     requests = SportsItemRequest.objects.all()

#     # Apply date filter if selected
#     if form.is_valid() and form.cleaned_data['start_date'] and form.cleaned_data['end_date']:
#         start_date = form.cleaned_data['start_date']
#         end_date = form.cleaned_data['end_date']
#         requests = requests.filter(request_date__range=[start_date, end_date])

#     # Apply category filter if selected
#     category_filter = form.cleaned_data.get('categories')
#     if category_filter:
#         requests = requests.filter(category=category_filter)

#     timestamps = [datetime.combine(request.request_date, datetime.min.time()) for request in requests]
#     request_counts = [requests.filter(request_date=request.request_date).count() for request in requests]

#     context = {
#         'form': form,
#         'timestamps': timestamps,
#         'request_counts': request_counts,
#     }
#     return render(request, 'sports_item_requests_trend_chart_view.html', context)

from django.shortcuts import render
from .forms import SportsItemRequestReceivedFilterForm
from .models import SportsItemRequest, SportsItemReceived

def sports_item_trend_chart_view(request):
    form = SportsItemRequestReceivedFilterForm(request.GET)
    requests = SportsItemRequest.objects.all()
    received_items = SportsItemReceived.objects.all()

    # Apply date filter if selected
    if form.is_valid() and form.cleaned_data['start_date'] and form.cleaned_data['end_date']:
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        requests = requests.filter(request_date__range=[start_date, end_date])
        received_items = received_items.filter(received_date__range=[start_date, end_date])

    # Apply category filter if selected
    category_filter = form.cleaned_data.get('categories')
    if category_filter:
        requests = requests.filter(category=category_filter)
        received_items = received_items.filter(category=category_filter)

    request_timestamps = [request.request_date for request in requests]
    request_counts = [requests.filter(request_date=request.request_date).count() for request in requests]

    received_timestamps = [received.received_date for received in received_items]
    received_counts = [received_items.filter(received_date=received.received_date).count() for received in received_items]

    context = {
        'form': form,
        'request_timestamps': request_timestamps,
        'request_counts': request_counts,
        'received_timestamps': received_timestamps,
        'received_counts': received_counts,
    }
    return render(request, 'sports_item_trend_chart_view.html', context)
from django.shortcuts import render
from .forms import SportsItemRequestStackedFilterForm
from .models import SportsItemRequest, Inventory_Stock
from django.db.models import Sum

def stacked_bar_chart_view(request):
    form = SportsItemRequestStackedFilterForm(request.GET)
    inventory_items = Inventory_Stock.objects.all()

    if form.is_valid():
        # Apply category filter if selected
        category_filter = form.cleaned_data.get('categories')
        if category_filter:
            inventory_items = inventory_items.filter(category=category_filter)

    item_names = [item.item_name for item in inventory_items]
    requested_quantities = [SportsItemRequest.objects.filter(item=item).aggregate(Sum('req_quantity'))['req_quantity__sum'] or 0 for item in inventory_items]
    issued_quantities = [SportsItemRequest.objects.filter(item=item, approval_status='I').aggregate(Sum('req_quantity'))['req_quantity__sum'] or 0 for item in inventory_items]
    remaining_quantities = [item.stock_quantity - issued_quantity for item, issued_quantity in zip(inventory_items, issued_quantities)]

    context = {
        'form': form,
        'item_names': item_names,
        'requested_quantities': requested_quantities,
        'issued_quantities': issued_quantities,
        'remaining_quantities': remaining_quantities,
    }
    return render(request, 'stacked_bar_chart_view.html', context)


from django.shortcuts import render
from .forms import SportsItemRequestReceivedFilterForm
from .models import SportsItemRequest, SportsItemReceived

def sports_item_time_series_chart_view(request):
    form = SportsItemRequestReceivedFilterForm(request.GET)
    requests = SportsItemRequest.objects.all()
    received_items = SportsItemReceived.objects.all()

    # Apply date filter if selected
    if form.is_valid() and form.cleaned_data['start_date'] and form.cleaned_data['end_date']:   #use cleaned for  sanitized and validate data
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        requests = requests.filter(request_date__range=[start_date, end_date])
        received_items = received_items.filter(received_date__range=[start_date, end_date])

    # Apply category filter if selected
    category_filter = form.cleaned_data.get('categories')
    if category_filter:
        requests = requests.filter(category=category_filter)
        received_items = received_items.filter(category=category_filter)

    request_timestamps = [request.request_date for request in requests]
    request_counts = [requests.filter(request_date=request.request_date).count() for request in requests]

    received_timestamps = [received.received_date for received in received_items]
    received_counts = [received_items.filter(received_date=received.received_date).count() for received in received_items]

    context = {
        'form': form,
        'request_timestamps': request_timestamps,
        'request_counts': request_counts,
        'received_timestamps': received_timestamps,
        'received_counts': received_counts,
    }
    return render(request, 'sports_item_time_series_chart_view.html', context)


#reports

from django.shortcuts import render
from django.http import HttpResponse
from .models import SportsItemRequest
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import csv

from django.http import FileResponse

def sports_item_request(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        generate_format = request.POST.get('generate')

        # Fetch item requests based on selected date range
        item_requests = SportsItemRequest.objects.filter(request_date__range=(start_date, end_date))

        if generate_format == 'pdf':
            # Generate PDF report
            pdf = generate_pdf(item_requests, start_date, end_date)
            if pdf:
                # Display the PDF in the browser
                return FileResponse(pdf, content_type='application/pdf')

        elif generate_format == 'csv':
            # Generate CSV report and return as a response
            csv_data = generate_csv(item_requests, start_date, end_date)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="sports_item_requests_{start_date}_to_{end_date}.csv"'
            response.write(csv_data)
            return response

    return render(request, 'sports_item_request.html')


def generate_pdf(request, start_date, end_date):
    item_requests = SportsItemRequest.objects.filter(request_date__range=(start_date, end_date))
    context = {
        'item_requests': item_requests,
        'start_date': start_date,
        'end_date': end_date,
    }

    html_string = render_to_string('sports_item_requests_pdf.html', context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=sports_item_requests_{start_date}_to_{end_date}.pdf'
    pisa_status = pisa.CreatePDF(html_string, dest=response)

    if pisa_status.err:
        return HttpResponse('PDF generation failed.')
    return response

def generate_csv(request, start_date, end_date):
    item_requests = SportsItemRequest.objects.filter(request_date__range=(start_date, end_date))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="sports_item_requests_{start_date}_to_{end_date}.csv"'

    writer = csv.writer(response)
    writer.writerow(['User', 'Category', 'Item', 'Request Date', 'Request Time', 'Requested Quantity', 'Request Type', 'Approval Status'])
    for item_request in item_requests:
        writer.writerow([
            item_request.user.username,
            item_request.category.category_name,
            item_request.item.item_name,
            item_request.request_date,
            item_request.request_time,
            item_request.req_quantity,
            dict(SportsItemRequest.TYPE_CHOICES).get(item_request.request_type),
            dict(SportsItemRequest.APPROVAL_CHOICES).get(item_request.approval_status),
        ])

    return response
