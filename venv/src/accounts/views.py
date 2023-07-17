
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



# views.py



User = get_user_model()

def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'No user with this email address.')
            return render(request, 'reset_password.html')

        # Generate a reset password token
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        # Send reset password email
        subject = 'Reset Your Password'
        message = render_to_string('reset_password_email.html', {
            'user': user,
            'uid': uid,
            'token': token,
        })
        from_email = 'your_email@gmail.com'  # Update with your email or use another method to get the sender's email
        send_mail(subject, message, from_email, [email])

        return redirect('reset_password_done')

    return render(request, 'reset_password.html')

def reset_password_done(request):
    return render(request, 'reset_password_done.html')

def reset_password_confirm(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            if password == confirm_password:
                user.set_password(password)
                user.save()
                messages.success(request, 'Password reset successfully.')
                return redirect('reset_password_complete')
            else:
                messages.error(request, 'Passwords do not match.')
    else:
        messages.error(request, 'Invalid reset link.')

    return render(request, 'reset_password_confirm.html')

def reset_password_complete(request):
    return render(request, 'reset_password_complete.html')
