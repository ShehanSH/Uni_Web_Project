from django.shortcuts import render
from .models import GroundBookingRequest,GroundBookingRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import GroundBookingRequestForm,GroundBookingRequestUpdateForm
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ground_booking.models import GroundBookingRequest  # Adjust the import path as per your project structure

# make a ground booking request.
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import GroundBookingRequestForm

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





def ground_booking_view(request):
    user = request.user
    requests = GroundBookingRequest.objects.filter(user=user)
    context = {
        
        "requests": requests
    }
    return render(request, 'list_bookings.html', context)



from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import GroundBookingRequestUpdateForm
from .models import GroundBookingRequest

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
            return redirect('ground_booking:ground_booking_request')

        else:
            messages.error(request, 'Error updating the ground booking request. Please check the form and try again.')
    
    else:
        form = GroundBookingRequestUpdateForm(instance=queryset)

    context = {
        'form': form
    }
    return render(request, 'update_ground_booking_request.html', context)



from django.contrib import messages
from django.shortcuts import redirect, render
from .models import GroundBookingRequest

def delete_booking_request(request, pk):
    try:
        queryset = GroundBookingRequest.objects.get(booking_id=pk)
    except GroundBookingRequest.DoesNotExist:
        messages.error(request, 'Ground booking request with the specified ID does not exist.')
        return redirect('ground_booking:ground_booking_request')

    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Ground booking request deleted successfully.')
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

from .models import Ground
from django.shortcuts import render, get_object_or_404
from .models import Ground

from django.shortcuts import render
from .models import Ground

def ground_details_view(request):
    all_grounds = Ground.objects.all()
    context = {
        "all_grounds": all_grounds
    }
    return render(request, 'ground_details.html', context)

