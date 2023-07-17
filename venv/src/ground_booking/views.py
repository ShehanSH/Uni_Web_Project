from django.shortcuts import render
from .models import GroundBookingRequest,GroundBookingRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import GroundBookingRequestForm
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