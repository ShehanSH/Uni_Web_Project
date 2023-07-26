
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





from typing import Protocol
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.db.models.query_utils import Q

from .forms import SetPasswordForm, PasswordResetForm
from .decorators import user_not_authenticated
from .tokens import account_activation_token


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


from .forms import SetPasswordForm

@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'password_reset_confirm.html', {'form': form})


from .forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from .decorators import user_not_authenticated
from django.shortcuts import render
from .decorators import user_not_authenticated
from .forms import PasswordResetForm  # Import your PasswordResetForm or any other necessary imports.

from .forms import PasswordResetForm
from django.db.models.query_utils import Q
...

@user_not_authenticated
def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                        """
                        <h2>Password reset sent</h2><hr>
                        <p>
                            We've emailed you instructions for setting your password, if an account exists with the email you entered. 
                            You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address 
                            you registered with, and check your spam folder.
                        </p>
                        """
                    )
                else:
                    messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")

            return redirect('homemain')

        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue

    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="password_reset.html", 
        context={"form": form}
        )



def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
                return redirect('homemain')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("homemain")




def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('homepage')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

from .models import CustomUser, Role, Faculty, Department, UniStudent, Outsider, UniStaff

@login_required
def user_profile(request):
    user = request.user
    context = {'user': user}

    if user.role_id == 2:
        # Get UniStudent details
        try:
            unistudent = UniStudent.objects.get(user=user)
            context['unistudent'] = unistudent
        except UniStudent.DoesNotExist:
            pass

    elif user.role_id == 3:
        # Get UniStaff details
        try:
            unistaff = UniStaff.objects.get(user=user)
            context['unistaff'] = unistaff
        except UniStaff.DoesNotExist:
            pass

    elif user.role_id == 4:
        # Get Outsider details
        try:
            outsider = Outsider.objects.get(user=user)
            context['outsider'] = outsider
        except Outsider.DoesNotExist:
            pass

    return render(request, 'user_profile.html', context)



from .models import CustomUser, UniStudent, UniStaff, Outsider
from .forms import CustomUserForm, UniStudentForm, UniStaffForm, OutsiderForm
@login_required
def edit_user_profile(request):
    user = request.user
    user_role_id = user.role_id

    # Get the relevant user instance based on role_id
    custom_user_instance = user
    uni_student_instance = UniStudent.objects.filter(user=user).first()
    uni_staff_instance = UniStaff.objects.filter(user=user).first()
    outsider_instance = Outsider.objects.filter(user=user).first()

    # Initialize the forms before the if blocks
    custom_user_form = CustomUserForm(request.POST or None, instance=custom_user_instance)
    uni_student_form = UniStudentForm(request.POST or None, instance=uni_student_instance)
    uni_staff_form = UniStaffForm(request.POST or None, instance=uni_staff_instance)
    outsider_form = OutsiderForm(request.POST or None, instance=outsider_instance)

    if request.method == 'POST':
        if user_role_id == 2:
            if custom_user_form.is_valid() and uni_student_form.is_valid():
                custom_user_form.save()
                uni_student_form.save()
                # Redirect to the user profile page after saving
                return redirect('user_profile')
        elif user_role_id == 3:
            if custom_user_form.is_valid() and uni_staff_form.is_valid():
                custom_user_form.save()
                uni_staff_form.save()
                # Redirect to the user profile page after saving
                return redirect('user_profile')
        elif user_role_id == 4:
            if custom_user_form.is_valid() and outsider_form.is_valid():
                custom_user_form.save()
                outsider_form.save()
                # Redirect to the user profile page after saving
                return redirect('user_profile')

    return render(request, 'edit_user_profile.html', {
        'custom_user_form': custom_user_form,
        'uni_student_form': uni_student_form,
        'uni_staff_form': uni_staff_form,
        'outsider_form': outsider_form,
    })


@login_required
def delete_user_profile(request):
    user = request.user
    if request.method == 'POST':
        # Delete the user account
        user.delete()
        return redirect('homemain')  # Redirect to the homepage or any other appropriate page

    context = {'user': user}
    return render(request, 'delete_user_profile.html', context)