
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

from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.shortcuts import render, redirect
from django.contrib import messages


def role(request):
    # Logic for role page
    return render(request, 'role.html')

#uni student
def uni_student_registration(request):
    if request.method == 'POST':
        registration_form = CustomRegistrationForm(request.POST)
        uni_student_form = UniStudentRegstrationForm(request.POST)
        
        try:
            if registration_form.is_valid() and uni_student_form.is_valid():
                # Check if the user selected the correct role (University Student)
                selected_role = registration_form.cleaned_data.get('role')
                if selected_role.role_name != 'University Student':
                    messages.error(request, "Please select 'University Student' as your user role.")
                    return redirect('uni_student_registration')
                
                user = registration_form.save()
                uni_student = uni_student_form.save(commit=False)
                uni_student.user = user
                uni_student.save()
                
                return redirect('login')
                
            else:
                # Handle form validation errors
                messages.error(request, "Please fill in fields correctly.")   
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
    else:
        registration_form = CustomRegistrationForm()
        uni_student_form =  UniStudentRegstrationForm()
      
    return render(request, 'uni_student_registration.html', {'registration_form': registration_form, 'uni_student_form': uni_student_form})

# uni staff
def uni_staff_registration(request):
    if request.method == 'POST':
        registration_form = CustomRegistrationForm(request.POST)
        uni_staff_form = UniStaffRegstrationForm(request.POST)
        
        try:
            if registration_form.is_valid() and uni_staff_form.is_valid():
                # Check if the user selected the correct role (University Staff)
                selected_role = registration_form.cleaned_data.get('role')
                if selected_role.role_name != 'University Staff':
                    messages.error(request, "Please select 'University Staff' as your user role.")
                    return redirect('uni_staff_registration')
                
                user = registration_form.save()
                uni_staff = uni_staff_form.save(commit=False)
                uni_staff.user = user
                uni_staff.save()
                
                return redirect('login')
                
            else:
                # Handle form validation errors
                messages.error(request, "Please fill in fields correctly.")   
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
    else:
        registration_form = CustomRegistrationForm()
        uni_staff_form = UniStaffRegstrationForm()
      
    return render(request, 'uni_staff_registration.html', {'registration_form': registration_form, 'uni_staff_form': uni_staff_form})
  

#outider
def outsider_registration(request):
    if request.method == 'POST':
        registration_form = CustomRegistrationForm(request.POST)
        outsider_form = OutsiderRegstrationForm(request.POST)
        
        try:
            if registration_form.is_valid() and outsider_form.is_valid():
                # Check if the user selected the correct role (Outsider)
                selected_role = registration_form.cleaned_data.get('role')
                if selected_role.role_name != 'Outsider':
                    messages.error(request, "Please select 'Outsider' as your user role.")
                    return redirect('outsider_registration')
                
                user = registration_form.save()
                outsider = outsider_form.save(commit=False)
                outsider.user = user
                outsider.save()
                
                return redirect('login')
                
            else:
                # Handle form validation errors
                messages.error(request, "Please fill in fields correctly.")   
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
    else:
        registration_form = CustomRegistrationForm()
        outsider_form = OutsiderRegstrationForm()
      
    return render(request, 'outsider_registration.html', {'registration_form': registration_form, 'outsider_form': outsider_form})



#login

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        
        # Check if the form fields are empty
        if not form.has_changed() or not form.is_valid():
            messages.error(request, 'Please enter the correct user credentials.')
        else:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homemain')  # Replace 'home' with your desired URL after login
            else:
                # Add an error message for invalid credentials
                messages.error(request, 'Invalid username or password.')
                
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



# views.py


# myapp/views.py

# accounts/views.py

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
# accounts/views.py

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'accounts/email/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'  # This was incorrect, remove this line
    template_name = 'accounts/password_reset_form.html'
    success_url = 'done/'
    subject = 'Password Reset Request'  # Set the email subject here

# Rest of the views remain the same...


class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'accounts/email/password_reset_email.html'
    subject_template_name = 'accounts/email/password_reset_subject.txt'
    template_name = 'accounts/password_reset_form.html'
    success_url = 'done/'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = '/accounts/reset/complete/'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

