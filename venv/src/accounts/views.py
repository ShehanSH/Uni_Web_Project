from django.shortcuts import render, redirect
from .models import User
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib import messages
from .forms import RegistrationForm, UniversityPersonForm, OutsiderForm
from .models import User, UniversityPerson, Outsider, Role, Faculty, Department
from .models import User, Role, Faculty, Department, UniversityPerson, Outsider
from .forms import RegistrationForm, UniversityPersonForm, OutsiderForm, LoginForm,RoleSelectionForm,UniversityStaffForm,UniversityStaffForm
import re
from django.core.exceptions import ValidationError
from django.contrib import messages
import re

from django.contrib import messages
import re

def role(request):
    # Logic for role page
    return render(request, 'role.html')

def test2(request):
    # Logic for role page
    return render(request, 'test2.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)
                role = user.role.role_name
               
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



def select_role(request):
    if request.method == 'POST':
        form = RoleSelectionForm(request.POST)
        if form.is_valid():
            role_id = form.cleaned_data['role_id']

            if role_id == 'university_person':
                return redirect('university_person_register')
            elif role_id == 'outsider':
                return redirect('outsider_register')
    else:
        form = RoleSelectionForm()

    return render(request, 'select_role.html', {'form': form})






def uni_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        university_form = UniversityPersonForm(request.POST)
        
        try:
            if form.is_valid() and university_form.is_valid():
                # Process the user registration form data
                username = form.cleaned_data['username']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                date_of_birth = form.cleaned_data['date_of_birth']
                phone_number = form.cleaned_data['phone_number']
                gender = form.cleaned_data['gender']
                address = form.cleaned_data['address']
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']
                role_id = form.cleaned_data['role_id'].role_id
                

                role = Role.objects.get(role_id=role_id)
                if role.role_name != 'University Person':
                    messages.error(request, "Select the University Person role for registration.")
                    return redirect('uni_registration')
                
                # Check if password and confirm password match
                if password != confirm_password:
                    messages.error(request, "Password and confirm password do not match.")
                    return redirect('uni_registration')
                
                # Name Validations
                if not first_name or not last_name:
                    messages.error(request, "Please enter both first name and last name.")
                    return redirect('uni_registration')
                
                # Date of Birth Validations
                if not date_of_birth:
                    messages.error(request, "Please enter your date of birth.")
                    return redirect('uni_registration')
                # Format: YYYY-MM-DD
                if not re.match(r'^\d{4}-\d{2}-\d{2}$', str(date_of_birth)):
                    messages.error(request, "Invalid date of birth format. Please use YYYY-MM-DD.")
                    return redirect('uni_registration')
                
                # Email Validations
                if not email:
                    messages.error(request, "Please enter your email address.")
                    return redirect('uni_registration')
                # Format: Email validation using a regular expression
                if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                    messages.error(request, "Invalid email address.")
                    return redirect('uni_registration')
                
                # Address Validations
                if not address:
                    messages.error(request, "Please enter your address.")
                    return redirect('uni_registration')
                # Length: Set a maximum limit for the address field
                if len(address) > 100:
                    messages.error(request, "Address is too long.")
                    return redirect('uni_registration')
                
                # Password Validations
                # Complexity: Minimum length, use of both letters and numbers, special characters
                if len(password) < 8:
                    messages.error(request, "Password must be at least 8 characters long.")
                    return redirect('uni_registration')
                if not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password) or not re.search(r'[^A-Za-z0-9]', password):
                    messages.error(request, "Password must contain at least one letter, one number, and one special character.")
                    return redirect('uni_registration')
                
                role = Role.objects.get(role_id=role_id)
                user = User(username=username, first_name=first_name, last_name=last_name,email=email,
                            date_of_birth=date_of_birth, phone_number=phone_number, gender=gender,
                            address=address, password=password, confirm_password=confirm_password, role=role)
                user.save()
                
                # Process the university person registration form data
                student_id = university_form.cleaned_data['student_id']
                faculty_id = university_form.cleaned_data['faculty_id']
                department_id = university_form.cleaned_data['department_id']

                faculty = Faculty.objects.get(faculty_id=faculty_id)
                department = Department.objects.get(department_id=department_id)
                
                university_person = UniversityPerson(student_id=student_id, faculty=faculty,
                                                     department=department, user_id=user)
                university_person.save()
                
                # messages.success(request, "Registration successful. You can now log in.")
                return redirect('login')
            else:
                messages.error(request, "Please fill in fields correctly.")
        
        except Exception as e:
            error_message = str(e)
            if 'Duplicate entry' in error_message:
                duplicate_entry = error_message.split("Duplicate entry ")[1].split(" for key")[0]
                messages.error(request, f"'{duplicate_entry}' already registered.")
            else:
                messages.error(request, "")
            print(error_message) 
        
    else:
        form = RegistrationForm()
        university_form = UniversityPersonForm()
        
    return render(request, 'uni_registration.html', {'form': form, 'university_form': university_form})

# uni_staff_registration

def uni_staff_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        staff_form = UniversityStaffForm(request.POST)
        
        try:
            if form.is_valid() and staff_form.is_valid():
                # Process the user registration form data
                username = form.cleaned_data['username']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                date_of_birth = form.cleaned_data['date_of_birth']
                phone_number = form.cleaned_data['phone_number']
                gender = form.cleaned_data['gender']
                address = form.cleaned_data['address']
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']
                role_id = form.cleaned_data['role_id'].role_id

                role = Role.objects.get(role_id=role_id)
                if role.role_name != 'University Staff':
                    messages.error(request, "Select the University Staff role for registration.")
                    return redirect('uni_staff_registration')

                # Check if password and confirm password match
                if password != confirm_password:
                    messages.error(request, "Password and confirm password do not match.")
                    return redirect('uni_staff_registration')

                # Name Validations
                if not first_name or not last_name:
                    messages.error(request, "Please enter both first name and last name.")
                    return redirect('uni_staff_registration')

                # Date of Birth Validations
                if not date_of_birth:
                    messages.error(request, "Please enter your date of birth.")
                    return redirect('uni_staff_registration')
                # Format: YYYY-MM-DD
                if not re.match(r'^\d{4}-\d{2}-\d{2}$', str(date_of_birth)):
                    messages.error(request, "Invalid date of birth format. Please use YYYY-MM-DD.")
                    return redirect('uni_staff_registration')

                # Email Validations
                if not email:
                    messages.error(request, "Please enter your email address.")
                    return redirect('uni_staff_registration')
                # Format: Email validation using a regular expression
                if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                    messages.error(request, "Invalid email address.")
                    return redirect('uni_staff_registration')

                # Address Validations
                if not address:
                    messages.error(request, "Please enter your address.")
                    return redirect('uni_staff_registration')
                # Length: Set a maximum limit for the address field
                if len(address) > 100:
                    messages.error(request, "Address is too long.")
                    return redirect('uni_staff_registration')

                # Password Validations
                # Complexity: Minimum length, use of both letters and numbers, special characters
                if len(password) < 8:
                    messages.error(request, "Password must be at least 8 characters long.")
                    return redirect('uni_staff_registration')
                if not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password) or not re.search(r'[^A-Za-z0-9]', password):
                    messages.error(request, "Password must contain at least one letter, one number, and one special character.")
                    return redirect('uni_staff_registration')

                role = Role.objects.get(role_id=role_id)
                user = User(username=username, first_name=first_name, last_name=last_name, email=email,
                            date_of_birth=date_of_birth, phone_number=phone_number, gender=gender,
                            address=address, password=password, confirm_password=confirm_password, role=role)
                user.save()

                # Process the university staff registration form data
                staff_id = staff_form.cleaned_data['staff_id']
                staff_type = staff_form.cleaned_data['staff_type']
                faculty_id = staff_form.cleaned_data['faculty_id']
                department_id = staff_form.cleaned_data['department_id']

                faculty = Faculty.objects.get(faculty_id=faculty_id)
                department = Department.objects.get(department_id=department_id)

                university_staff_person = UniversityStaffForm(staff_id=staff_id, user_id=user,
                                                                department=department, faculty=faculty, staff_type=staff_type)
                university_staff_person.save()

                # messages.success(request, "Registration successful. You can now log in.")
                return redirect('login')
            else:
                messages.error(request, "Please fill in fields correctly.")

        except Exception as e:
            error_message = str(e)
            if 'Duplicate entry' in error_message:
                duplicate_entry = error_message.split("Duplicate entry ")[1].split(" for key")[0]
                messages.error(request, f"'{duplicate_entry}' already registered.")
            else:
                messages.error(request, "trtururt")
            print(error_message)

    else:
        form = RegistrationForm()
        staff_form = UniversityStaffForm()

    return render(request, 'uni_staff_registration.html', {'form': form, 'staff_form': staff_form})

#outsider form


def outsider_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        outsider_form = OutsiderForm(request.POST)
        
        try:
            if form.is_valid() and outsider_form.is_valid():
                # Process the user registration form data
                username = form.cleaned_data['username']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                date_of_birth = form.cleaned_data['date_of_birth']
                phone_number = form.cleaned_data['phone_number']
                gender = form.cleaned_data['gender']
                address = form.cleaned_data['address']
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']
                role_id = form.cleaned_data['role_id'].role_id

                role = Role.objects.get(role_id=role_id)
                if role.role_name != 'Outsider':
                    messages.error(request, "Select the outsider role for registration.")
                    return redirect('outsider_registration')
                
                # Check if password and confirm password match
                if password != confirm_password:
                    messages.error(request, "Password and confirm password do not match.")
                    return redirect('outsider_registration')
                
                # Name Validations
                if not first_name or not last_name:
                    messages.error(request, "Please enter both first name and last name.")
                    return redirect('outsider_registration')
                
                if not email:
                    messages.error(request, "Please enter your email address.")
                    return redirect('outsider_registration')
                # Format: Email validation using a regular expression
                if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                    messages.error(request, "Invalid email address.")
                    return redirect('outsider_registration')
                
                
                # Date of Birth Validations
                if not date_of_birth:
                    messages.error(request, "Please enter your date of birth.")
                    return redirect('outsider_registration')
                # Format: YYYY-MM-DD
                date_of_birth_str = date_of_birth.strftime('%Y-%m-%d')
    
                # Format: YYYY-MM-DD
                if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_of_birth_str):
                    messages.error(request, "Invalid date of birth format. Please use YYYY-MM-DD.")
                    return redirect('outsider_registration')
                    
                # Address Validations
                if not address:
                    messages.error(request, "Please enter your address.")
                    return redirect('outsider_registration')
                # Length: Set a maximum limit for the address field
                if len(address) > 100:
                    messages.error(request, "Address is too long.")
                    return redirect('outsider_registration')
                
                # Password Validations
                # Complexity: Minimum length, use of both letters and numbers, special characters
                if len(password) < 8:
                    messages.error(request, "Password must be at least 8 characters long.")
                    return redirect('outsider_registration')
                if not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password) or not re.search(r'[^A-Za-z0-9]', password):
                    messages.error(request, "Password must contain at least one letter, one number, and one special character.")
                    return redirect('outsider_registration')
            
                
                user = User(username=username, first_name=first_name, last_name=last_name, email=email,
                            date_of_birth=date_of_birth, phone_number=phone_number, gender=gender,
                            address=address, password=password, confirm_password=confirm_password, role=role)
                user.save()
                
                # Process the outsider registration form data
                nic = outsider_form.cleaned_data['nic']
                outsider_person = Outsider(nic=nic, user_id=user)
                outsider_person.save()
                
                # messages.success(request, "Registration successful. You can now log in.")
                return redirect('login')
            else:
                messages.error(request, "Please fill in fields correctly.")
        except Exception as e:
                    error_message = str(e)
                    if 'Duplicate entry' in error_message:
                        duplicate_entry = error_message.split("Duplicate entry ")[1].split(" for key")[0]
                        messages.error(request, f"'{duplicate_entry}' already registered.")
                    else:
                        messages.error(request, "")
                    print(error_message) 
 
    else:
        form = RegistrationForm()
        outsider_form = OutsiderForm()

    return render(request, 'outsider_registration.html', {'form': form, 'outsider_form': outsider_form})




# def outsider_registration(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         outsider_form = OutsiderForm(request.POST)

#         if form.is_valid() and outsider_form.is_valid():
#             # Process the user registration form data
#             username = form.cleaned_data['username']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             password = form.cleaned_data['password']
#             role_id = form.cleaned_data['role_id'].role_id
#             email = form.cleaned_data['email']
            
#             role = Role.objects.get(role_id=role_id)
#             if role.role_name != 'Outsider':
#                 messages.error(request, "Select the outsider role for registration.")
#                 return redirect('outsider_registration')
            
#             email = form.cleaned_data['email']
#             if User.objects.filter(email=email).exists():
#                 messages.error(request, "Email address is already registered.")
#                 return redirect('outsider_registration')
            
#             user = User(username=username, first_name=first_name, last_name=last_name, password=password, role=role, email=email)
#             user.save()
            
#             # Process the outsider registration form data
#             nic = outsider_form.cleaned_data['nic']
#             outsider_person = Outsider(nic=nic, user_id=user)
#             outsider_person.save()
            
#             messages.success(request, "Registration successful. You can now log in.")
#             return redirect('login')
        
#         else:
#             messages.error(request, "Please fill in all fields.")
    
#     else:
#         form = RegistrationForm()
#         outsider_form = OutsiderForm()
    
#     return render(request, 'outsider_registration.html', {'form': form, 'outsider_form': outsider_form})






def admin(request):
    # Logic for admin page
    return render(request, 'admin.html')

def uniPerson(request):
    # Logic for university page
    return render(request, 'uniPerson.html')

def outsider(request):
    # Logic for outsider page
    return render(request, 'outsider.html')


