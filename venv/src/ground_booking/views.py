
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
        ground_bookings = ground_bookings.filter(ground=ground_name_filter)

    # Apply event name filter if selected
    event_name_filter = form.cleaned_data.get('event_name')
    if event_name_filter:
        ground_bookings = ground_bookings.filter(event=event_name_filter)

    # Create a defaultdict to store the count of booking requests per ground
    booking_count_per_ground = defaultdict(int)

    for booking in ground_bookings:
        ground_name = booking.ground.ground_name
        booking_count_per_ground[ground_name] += 1

    # Prepare data for the Plotly bar chart
    ground_names = list(booking_count_per_ground.keys())
    booking_counts = list(booking_count_per_ground.values())
    custom_colors = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)', 'rgb(44, 160, 44)', 'rgb(214, 39, 40)']
    # Create the trace for the bar chart
    trace = go.Bar(x=ground_names, y=booking_counts, marker=dict(color=custom_colors))

    # Prepare the data for the chart
    data = [trace]

    # Layout for the bar chart
    layout = go.Layout(
        title='Number of Ground Booking Requests per Ground',
        xaxis=dict(title='Ground Names'),
        yaxis=dict(title='Number of Booking Requests')
    )

    # Render the bar chart
    chart = go.Figure(data=data, layout=layout)
    chart_div = chart.to_html(full_html=False)

    context = {
        'form': form,
        'chart_div': chart_div
    }

    return render(request, 'ground_booking_bar_chart_view.html', context)


#chart 2
# views.py
from django.shortcuts import render
from .models import GroundBookingRequest
from .forms import GroundBookingFilterForm
import plotly.graph_objs as go

def ground_booking_stacked_bar_chart_view(request):
    form = GroundBookingFilterForm(request.GET)
    bookings = GroundBookingRequest.objects.all()

    # Apply filters if provided
    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        event_name = form.cleaned_data.get('event_name')

        if start_date:
            bookings = bookings.filter(request_date__gte=start_date)
        if end_date:
            bookings = bookings.filter(request_date__lte=end_date)
        if event_name:
            bookings = bookings.filter(event__event_name=event_name)

    # Group bookings by ground and approval status
    ground_booking_counts = {}
    ground_names = set()
    approval_statuses = ['Approval', 'Disapproval']

    for booking in bookings:
        ground_name = booking.ground.ground_name
        approval_status = 'Approval' if booking.approval_status == 'A' else 'Disapproval'
        ground_booking_counts.setdefault(ground_name, {})
        ground_booking_counts[ground_name].setdefault(approval_status, 0)
        ground_booking_counts[ground_name][approval_status] += 1
        ground_names.add(ground_name)

    # Prepare data for the stacked bar chart
    data = []
    for approval_status in approval_statuses:
        counts = [ground_booking_counts[ground_name].get(approval_status, 0) for ground_name in ground_names]
        data.append(go.Bar(name=approval_status, x=list(ground_names), y=counts))

    # Layout for the stacked bar chart
    layout = go.Layout(
        title='Number of Booking Requests per Ground (Grouped by Approval Status)',
        xaxis=dict(title='Ground Names'),
        yaxis=dict(title='Number of Booking Requests'),
        barmode='stack'  # Use 'stack' for stacked bars
    )

    # Render the stacked bar chart
    chart = go.Figure(data=data, layout=layout)
    chart_div = chart.to_html(full_html=False)

    context = {
        'form': form,
        'chart_div': chart_div
    }

    return render(request, 'ground_booking_stacked_bar_chart_view.html', context)


#chart 3
from django.shortcuts import render
from .models import GroundBookingRequest
from .forms import GroundBookingFilterForm
from datetime import timedelta
import plotly.graph_objs as go

def ground_booking_line_chart_view(request):
    # Retrieve data from the model
    queryset = GroundBookingRequest.objects.all()

    # Handle filters using the form
    form = GroundBookingFilterForm(request.GET)
    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        event_name = form.cleaned_data.get('event_name')

        if start_date:
            queryset = queryset.filter(request_date__gte=start_date)
        if end_date:
            queryset = queryset.filter(request_date__lte=end_date)
        if event_name:
            queryset = queryset.filter(event__event_name=event_name)

    # Check if the queryset is empty
    if not queryset:
        context = {
            'form': form,
            'error_message': "No data available for the selected filters.",
        }
        return render(request, 'ground_booking_line_chart_view.html', context)

    # Prepare data for the Plotly line chart
    dates = [queryset.first().request_date + timedelta(days=x) for x in range((queryset.last().request_date - queryset.first().request_date).days + 1)]
    request_counts = [queryset.filter(request_date=date).count() for date in dates]

    # Create the trace for the line chart
    trace = go.Scatter(x=dates, y=request_counts, mode='lines+markers')

    # Prepare the data for the chart
    data = [trace]

    # Layout for the line chart
    layout = go.Layout(
        title='Booking Requests Trend',
        xaxis=dict(title='Request Date'),
        yaxis=dict(title='Number of Booking Requests per Day'),
    )

    # Render the line chart
    chart = go.Figure(data=data, layout=layout)
    chart_div = chart.to_html(full_html=False)

    context = {
        'form': form,
        'chart_div': chart_div
    }

    return render(request, 'ground_booking_line_chart_view.html', context)
