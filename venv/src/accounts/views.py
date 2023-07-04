from django.shortcuts import render, redirect
from .models import User
from .forms import RegistrationForm, LoginForm
from django.contrib import messages


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




def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
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
            # Check if the form has been submitted
            if 'username' in request.POST and 'password' in request.POST:
                error_message = list(form.errors.values())[0][0]
                messages.error(request, error_message)
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


# def register_uniPerson(request):
#     role = request.GET.get('role', '')  # Get the role query parameter

#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             role = form.cleaned_data['role']
           
#             # Get the role ID from the selected Role object
#             role_id = role.id

#             user = User(username=username, password=password, role_id=role_id)
#             user.save()

#             # Redirect to login page or any other page as desired
#             return redirect('login')
#     else:
#         initial = {'role': role}  # Set the initial value for the role field
#         form = RegistrationForm(initial=initial)

#     return render(request, 'uni_register.html', {'form': form})


def register_uniPerson(request):
    role = request.GET.get('role', '')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date_of_birth = form.cleaned_data['date_of_birth']
            gender = form.cleaned_data['gender']
            phone_number = form.cleaned_data['phone_number']
            faculty = form.cleaned_data['faculty']
            department = form.cleaned_data['department']
            confirm_password = form.cleaned_data['confirm_password']
            role = form.cleaned_data['role']

            role_id = role.id

            user = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                date_of_birth=date_of_birth,
                gender=gender,
                phone_number=phone_number,
                faculty=faculty,
                department=department,
                password=password,
                role_id=role_id
            )
            user.save()

            return redirect('login')
    else:
        initial = {'role': role}
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