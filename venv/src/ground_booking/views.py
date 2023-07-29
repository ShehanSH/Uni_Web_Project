
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import GroundBookingRequestForm, GroundBookingRequestUpdateForm
from .models import GroundBookingRequest, Ground

#ground booking request
@login_required(login_url='login')
def ground_booking_request(request):
    if request.method == 'POST':
        form = GroundBookingRequestForm(request.POST, request.FILES)
        if form.is_valid():
            ground_booking_request = form.save(commit=False)
            ground_booking_request.user = request.user
            file2 = request.FILES.get('event_form')
            if file2:
                ground_booking_request.event_form = file2
            ground_booking_request.save()
            messages.success(request, 'Ground booking request submitted successfully.')
            return redirect('ground_booking:ground_booking_request')
        else:
            messages.error(request, 'Error submitting the ground booking request. Please check the form and try again.')
    else:
        form = GroundBookingRequestForm()

    return render(request, 'ground_booking_request.html', {'form': form})

#view ground booking request
def ground_booking_view(request):
    user = request.user
    requests = GroundBookingRequest.objects.filter(user=user)
    context = {
        
        "requests": requests
    }
    return render(request, 'list_bookings.html', context)

#update ground booking request
def update_ground_booking_request(request, pk):
    try:
        queryset = GroundBookingRequest.objects.get(booking_id=pk)
    except GroundBookingRequest.DoesNotExist:
        messages.error(request, 'Ground booking request with the specified ID does not exist.')
        return redirect('ground_booking:ground_booking_request')

    if request.method == 'POST':
        form = GroundBookingRequestUpdateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            # Check if a new file was uploaded
            file2 = request.FILES.get('event_form')
            if file2:
                queryset.event_form = file2

            form.save()
            messages.success(request, 'Ground booking request updated successfully.')
            return redirect('ground_booking:list_booking')

        else:
            messages.error(request, 'Error updating the ground booking request. Please check the form and try again.')
    
    else:
        form = GroundBookingRequestUpdateForm(instance=queryset)

    context = {
        'form': form
    }
    return render(request, 'update_ground_booking_request.html', context)


#delete ground booking request
def delete_booking_request(request, pk):
    try:
        queryset = GroundBookingRequest.objects.get(booking_id=pk)
    except GroundBookingRequest.DoesNotExist:
        messages.error(request, 'Ground booking request with the specified ID does not exist.')
        return redirect('ground_booking:ground_booking_request')

    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Ground booking request deleted successfully.')
        return redirect('ground_booking:list_booking')
        
    return render(request, 'delete_booking_request.html')


#calendar view
def calendar_view(request):
    return render(request, 'calendar.html')

#all events
def all_events(request):
    # Retrieve all GroundBookingRequest objects
    bookings = GroundBookingRequest.objects.all()

    # Prepare a list to store events
    events = []

    for booking in bookings:
        # Format the event start time
        start = booking.request_date.strftime('%Y-%m-%d') + 'T' + booking.request_time.strftime('%H:%M:%S')

        # Add the event data to the list
        events.append({
            'title': str(booking.ground),
            'start': start,
            'approval_status': booking.approval_status,
        })

    # Return the events as a JSON response
    return JsonResponse(events, safe=False)

#ground details
def ground_details_view(request):
    all_grounds = Ground.objects.all()
    context = {
        "all_grounds": all_grounds
    }
    return render(request, 'ground_details.html', context)



#chart 1
from django.shortcuts import render
from .models import GroundBookingRequest
from .forms import GroundBookingFilterForm
import plotly.graph_objs as go
from collections import defaultdict

def ground_booking_bar_chart_view(request):
    form = GroundBookingFilterForm(request.GET)
    ground_bookings = GroundBookingRequest.objects.all()

    # Apply date filter if selected
    if form.is_valid() and form.cleaned_data['start_date'] and form.cleaned_data['end_date']:
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        ground_bookings = ground_bookings.filter(request_date__range=[start_date, end_date])

    # Apply ground name filter if selected
    ground_name_filter = form.cleaned_data.get('ground_name')
    if ground_name_filter:
        ground_bookings = ground_bookings.filter(ground__ground_name=ground_name_filter)

    # Create a defaultdict to store the sum of request quantity for each event and approval status
    request_quantity_sum = defaultdict(int)

    for booking in ground_bookings:
        event_name = booking.event.event_name
        approval_status = booking.get_approval_status_display()

        # Add the request quantity to the specific event and approval status
        request_quantity_sum[(event_name, approval_status)] += booking.request_quantity

    # Prepare data for the Plotly bar chart
    event_names = []
    approval_statuses = []
    request_quantities = []

    for (event_name, approval_status), quantity_sum in request_quantity_sum.items():
        event_names.append(event_name)
        approval_statuses.append(approval_status)
        request_quantities.append(quantity_sum)

    # Create traces for each approval status
    trace_approval = go.Bar(x=event_names, y=request_quantities, name='Approval', marker=dict(color='green'))

    # Prepare the data for the chart
    data = [trace_approval]

    # Layout for the bar chart
    layout = go.Layout(
        title='Ground Booking Requests by Approval Status',
        xaxis=dict(title='Event Names'),
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

    return render(request, 'ground_booking_bar_chart_view.html', context)
