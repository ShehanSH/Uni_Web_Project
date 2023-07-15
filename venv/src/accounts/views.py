
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
        
        if registration_form.is_valid() and uni_staff_form.is_valid():
            user = registration_form.save()
            
            outsider = outsider_form.save(commit=False)
            outsider.user = user
            outsider.save()
            
            return redirect('login')
            
        else:
            messages.error(request, "Please fill in fields correctly.")   
    else:
        registration_form = CustomRegistrationForm()
        uni_staff_form = UniStaffRegstrationForm()
      
    return render(request, 'outsider_registration.html', {'registration_form': registration_form, 'uni_staff_form': uni_staff_form})





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





from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm, UniStudentRegstrationForm,Role
from django.contrib import messages
import re 
def registration_view(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        uniform = UniStudentRegstrationForm(request.POST)
        
        if form.is_valid() and uniform.is_valid():
                form.save()
                uniform.save()  # Add this line to save the uniform data
                return redirect('login')  # Replace 'login' with your desired URL after successful registration
    else:
        form = CustomRegistrationForm()
        uniform = UniStudentRegstrationForm()
    
    return render(request, 'uni_registration.html', {'form': form, 'uniform': uniform})

    


def home2nd(request):
    # Logic for admin page
    return render(request, 'home2nd.html')

def homemain(request):
  
    context = {
        
    }
    return render(request, 'homemain.html', context)


# def uni_reg(request):
#     # Logic for university page
#     if request.method == 'POST':
#         uniform = UniStudentRegstrationForm(request.POST)
#         if uniform.is_valid():
#             uniform.save()
#             return redirect('login')  # Replace 'login' with your desired URL after successful registration
#     else:
#         uniform = UniStudentRegstrationForm()
#     return render(request, 'uni_reg.html', {'form': uniform})


# def registration_view(request):
#     if request.method == 'POST':
#         form = CustomRegistrationForm(request.POST)
#         university_form = UniStudentRegstrationForm(request.POST)
        
#         try:
#             if form.is_valid() and university_form.is_valid():
#                 # Process the user registration form data
#                 username = form.cleaned_data['username']
#                 first_name = form.cleaned_data['first_name']
#                 last_name = form.cleaned_data['last_name']
#                 email = form.cleaned_data['email']
#                 date_of_birth = form.cleaned_data['date_of_birth']
#                 phone_number = form.cleaned_data['phone_number']
#                 gender = form.cleaned_data['gender']
#                 address = form.cleaned_data['address']
#                 password = form.cleaned_data['password']
#                 confirm_password = form.cleaned_data['confirm_password']
#                 # role_id = form.cleaned_data['role_id'].role_id
                

#                 # role = Role.objects.get(role_id=role_id)
#                 # if role.role_name != 'University Student':
#                 #     messages.error(request, "Select the University Person role for registration.")
#                 #     return redirect('uni_registration')
                
                
#                 # role = Role.objects.get(role_id=role_id)
#                 user = CustomUser(username=username, first_name=first_name, last_name=last_name,email=email,
#                             date_of_birth=date_of_birth, phone_number=phone_number, gender=gender,
#                             address=address, password=password, confirm_password=confirm_password, role=role)
#                 user.save()
                
#                 # Process the university person registration form data
#                 student_id = university_form.cleaned_data['student_id']
#                 faculty_id = university_form.cleaned_data['faculty_id']
#                 department_id = university_form.cleaned_data['department_id']

#                 faculty = Faculty.objects.get(faculty_id=faculty_id)
#                 department = Department.objects.get(department_id=department_id)
                
#                 university_person = UniStudent(student_id=student_id, faculty=faculty,
#                                                      department=department, user_id=user)
#                 university_person.save()
                
#                 # messages.success(request, "Registration successful. You can now log in.")
#                 return redirect('login')
#             else:
#                 messages.error(request, "Please fill in fields correctly.")
        
#         except Exception as e:
#             error_message = str(e)
#             if 'Duplicate entry' in error_message:
#                 duplicate_entry = error_message.split("Duplicate entry ")[1].split(" for key")[0]
#                 messages.error(request, f"'{duplicate_entry}' already registered.")
#             else:
#                 messages.error(request, "")
#             print(error_message) 
        
#     else:
#         form =  CustomLoginForm()
#         university_form = UniStudentRegstrationForm()
        
#     return render(request, 'uni_registration.html', {'form': form, 'university_form':university_form})