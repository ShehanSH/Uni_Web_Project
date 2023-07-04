from django.shortcuts import render, redirect
from .models import User
from .forms import RegistrationForm, LoginForm

from .forms import RegistrationForm, LoginForm

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         try:
#             user = User.objects.get(username=username, password=password)
#             role = user.role.role_name
#             role_id = user.role.id
#             if role == 'Admin':
#                 return redirect('admin')
#             elif role == 'University Person':
#                 return redirect('uniPerson')
#             elif role == 'Outsider':
#                 return redirect('outsider')
#         except User.DoesNotExist:
#             error_message = 'Invalid username or password. Please try again.'
#             return render(request, 'login.html', {'error_message': error_message})
#     return render(request, 'login.html')


from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Add form validation
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=username, password=password)
                role = user.role.role_name
                role_id = user.role.id
                if role == 'Admin':
                    return redirect('admin')
                elif role == 'University Person':
                    return redirect('uniPerson')
                elif role == 'Outsider':
                    return redirect('outsider')
            except User.DoesNotExist:
                error_message = 'Invalid username or password. Please try again.'
                messages.error(request, error_message)
        else:
            # Form is not valid, display form errors
            for field, errors in form.errors.items():
                for error in errors:
                    error = 'Feilds cannot be empty. Please try again.'
                    messages.error(request, error)
    
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})



def role(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'Admin':
            return redirect('admin_registration')
        elif role == 'University Person':
            return redirect('university_person_registration')
        elif role == 'outsider':
            return redirect('outsider_registration')
    return render(request, 'role.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            
            if role == 'Admin':
                return register_admin(request, form)
            elif role == 'University Person':
                return register_uniPerson(request, form)
            elif role == 'Outsider':
                return register_outsider(request, form)
        else:
            messages.error(request, 'Invalid form submission')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def register_admin(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
           
            # Get the role ID from the selected Role object
            role_id = role.id

            user = User(username=username, password=password, role_id=role_id)
            user.save()

            # Redirect to login page or any other page as desired
            return redirect('login')
    else:
        initial = {'role': role}  # Set the initial value for the role field
        form = RegistrationForm(initial=initial)

    return render(request, 'admin_register.html', {'form': form})


def register_uniPerson(request):
    role = request.GET.get('role', '')  # Get the role query parameter

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
           
            # Get the role ID from the selected Role object
            role_id = role.id

            user = User(username=username, password=password, role_id=role_id)
            user.save()

            # Redirect to login page or any other page as desired
            return redirect('login')
    else:
        initial = {'role': role}  # Set the initial value for the role field
        form = RegistrationForm(initial=initial)

    return render(request, 'uni_register.html', {'form': form})



def register_outsider(request):
    role = request.GET.get('role', '')  # Get the role query parameter

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
           
            # Get the role ID from the selected Role object
            role_id = role.id

            user = User(username=username, password=password, role_id=role_id)
            user.save()

            # Redirect to login page or any other page as desired
            return redirect('login')
    else:
        initial = {'role': role}  # Set the initial value for the role field
        form = RegistrationForm(initial=initial)

    return render(request, 'outsider_register.html', {'form': form})





def admin(request):
    # Logic for admin page
    return render(request, 'admin.html')

def uniPerson(request):
    # Logic for university page
    return render(request, 'uniPerson.html')

def outsider(request):
    # Logic for outsider page
    return render(request, 'outsider.html')