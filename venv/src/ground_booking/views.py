from django.shortcuts import render
from .models import GroundBookingRequest,GroundBookingRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import GroundBookingRequestForm,GroundBookingRequestUpdateForm
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# make a ground booking request.
@login_required(login_url='login')
def ground_booking_request(request):
    if request.method == 'POST':
        form = GroundBookingRequestForm(request.POST)
        if form.is_valid():
            ground_booking_request = form.save(commit=False)
            ground_booking_request.user = request.user
            ground_booking_request.save()
            # Redirect to a success page or perform any other desired action
            return redirect('ground_booking:ground_booking_request')
    else:
        form = GroundBookingRequestForm()

    return render(request, 'ground_booking_request.html', {'form': form})



def ground_booking_view(request):
    user = request.user
    requests = GroundBookingRequest.objects.filter(user=user)
    context = {
        
        "requests": requests
    }
    return render(request, 'list_bookings.html', context)



def update_ground_booking_request(request, pk):
    queryset = GroundBookingRequest.objects.get(booking_id=pk)
    form = GroundBookingRequestUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = GroundBookingRequestUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Item updated successfully')
            return redirect('ground_booking:ground_booking_request')

    context = {
        'form': form
    }
    return render(request, 'update_ground_booking_request.html', context)


def delete_booking_request(request, pk):
    queryset = GroundBookingRequest.objects.get(booking_id=pk)
    if request.method == 'POST':
        queryset.delete()
        # messages.success(request, 'Item deleted successfully')        #ADD MESSAGES OF ALL VIEWWWSSSSSSSSSSSSSSSSSS
        return redirect('ground_booking:ground_booking_request')
    return render(request, 'delete_booking_request.html')

from django.http import JsonResponse
from django.shortcuts import render
from .models import GroundBookingRequest

from django.shortcuts import render
from django.http import JsonResponse
from .models import GroundBookingRequest

def calendar_view(request):
    return render(request, 'calendar.html')

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
