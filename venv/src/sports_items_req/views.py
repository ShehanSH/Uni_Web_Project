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


def list_requests_view(request):
    user = request.user
    requests = SportsItemRequest.objects.filter(user=user)
    context = {
        "requests": requests
    }
    return render(request, 'list_requests.html', context)


from django.shortcuts import render, get_object_or_404, redirect
from .models import SportsItemRequest
from .forms import SportsItemsRequestForm

def update_sports_item_request(request, request_id):
    sports_item_request = get_object_or_404(SportsItemRequest, request_id=request_id)

    if request.method == 'POST':
        form = SportsItemsRequestForm(request.POST, instance=sports_item_request)
        if form.is_valid():
            form.save()
            return redirect('list_requests')
    else:
        form = SportsItemsRequestForm(instance=sports_item_request)

    context = {
        'form': form,
        'request_id': request_id,
    }

    return render(request, 'update_sports_item_request.html', context)
