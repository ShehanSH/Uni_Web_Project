
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomLoginForm, CustomRegistrationForm, UniStudentRegstrationForm
from .models import CustomUser, Role, Faculty, Department, UniStudent, Outsider
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm, CustomLoginForm, UniStudentRegstrationForm, UniStaffRegstrationForm, OutsiderRegstrationForm
from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm, UniStudentRegstrationForm,Role
from django.contrib import messages
import re 


def role(request):
    # Logic for role page
    return render(request, 'role.html')

def uni_student_registration(request):
    if request.method == 'POST':
        registration_form = CustomRegistrationForm(request.POST)
        uni_student_form = UniStudentRegstrationForm(request.POST)
        
        if registration_form.is_valid() and uni_student_form.is_valid():
            # Save the registration form data
            user = registration_form.save()
            
            # Create the UniStudent instance and associate it with the user
            uni_student = uni_student_form.save(commit=False)
            uni_student.user = user
            uni_student.save()
            
            # Redirect to the appropriate page based on the user's role
            # role_name = user.role.role_name
            # if role_name == 'Admin':
            #     return redirect('admin_page')
            # elif role_name == 'University student':
            return redirect('login')
                
            # Handle other role-specific redirects or error messages as needed
            
        else:
            # Handle form validation errors
            messages.error(request, "Please fill in fields correctly.")   
    else:
        registration_form = CustomRegistrationForm()
        uni_student_form = UniStudentRegstrationForm()
      
    return render(request, 'uni_student_registration.html', {'registration_form': registration_form, 'uni_student_form': uni_student_form})

# uni staff
def uni_staff_registration(request):
    if request.method == 'POST':
        registration_form = CustomRegistrationForm(request.POST)
        uni_staff_form = UniStaffRegstrationForm(request.POST)
        
        if registration_form.is_valid() and uni_staff_form.is_valid():
            user = registration_form.save()
            
            uni_staff = uni_staff_form.save(commit=False)
            uni_staff.user = user
            uni_staff.save()
            
            return redirect('login')
            
        else:
            messages.error(request, "Please fill in fields correctly.")   
    else:
        registration_form = CustomRegistrationForm()
        uni_staff_form = UniStaffRegstrationForm()
      
    return render(request, 'uni_staff_registration.html', {'registration_form': registration_form, 'uni_staff_form': uni_staff_form})

#outider

def outsider_registration(request):
    if request.method == 'POST':
        registration_form = CustomRegistrationForm(request.POST)
        outsider_form = OutsiderRegstrationForm(request.POST)
        
        if registration_form.is_valid() and outsider_form.is_valid():
            user = registration_form.save()
            
            outsider = outsider_form.save(commit=False)
            outsider.user = user
            outsider.save()
            
            return redirect('login')
            
        else:
            messages.error(request, "Please fill in fields correctly.")   
    else:
        registration_form = CustomRegistrationForm()
        outsider_form = OutsiderRegstrationForm()
      
    return render(request, 'outsider_registration.html', {'registration_form': registration_form, 'outsider_form': outsider_form})


#login

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homemain')  # Replace 'home' with your desired URL after login
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


#registration

# def registration_view(request):
#     if request.method == 'POST':
#         form = CustomRegistrationForm(request.POST)
#         uniform = UniStudentRegstrationForm(request.POST)
        
#         if form.is_valid() and uniform.is_valid():
#                 form.save()
#                 uniform.save()  # Add this line to save the uniform data
#                 return redirect('login')  # Replace 'login' with your desired URL after successful registration
#     else:
#         form = CustomRegistrationForm()
#         uniform = UniStudentRegstrationForm()
    
#     return render(request, 'uni_registration.html', {'form': form, 'uniform': uniform})

    



# def homemain(request):
  
#     context = {
        
#     }
#     return render(request, 'homemain.html', context)
