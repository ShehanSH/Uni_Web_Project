from django.shortcuts import render, redirect
from .models import User
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib import messages
from .forms import RegistrationForm, UniversityPersonForm, OutsiderForm
from .models import User, UniversityPerson, Outsider, Role, Faculty, Department
from .models import User, Role, Faculty, Department, UniversityPerson, Outsider
from .forms import RegistrationForm, UniversityPersonForm, OutsiderForm, LoginForm,RoleSelectionForm


def role(request):
    # Logic for role page
    return render(request, 'role.html')


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





from django.contrib import messages
import re

def uni_register(request):
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
                
                # Check if password and confirm password match
                if password != confirm_password:
                    messages.error(request, "Password and confirm password do not match.")
                    return redirect('uni_register')
                
                # Name Validations
                if not first_name or not last_name:
                    messages.error(request, "Please enter both first name and last name.")
                    return redirect('uni_register')
                
                # Date of Birth Validations
                if not date_of_birth:
                    messages.error(request, "Please enter your date of birth.")
                    return redirect('uni_register')
                # Format: YYYY-MM-DD
                if not re.match(r'^\d{4}-\d{2}-\d{2}$', str(date_of_birth)):
                    messages.error(request, "Invalid date of birth format. Please use YYYY-MM-DD.")
                    return redirect('uni_register')
                
                # Email Validations
                if not email:
                    messages.error(request, "Please enter your email address.")
                    return redirect('uni_register')
                # Format: Email validation using a regular expression
                if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                    messages.error(request, "Invalid email address.")
                    return redirect('uni_register')
                
                # Address Validations
                if not address:
                    messages.error(request, "Please enter your address.")
                    return redirect('uni_register')
                # Length: Set a maximum limit for the address field
                if len(address) > 100:
                    messages.error(request, "Address is too long.")
                    return redirect('uni_register')
                
                # Password Validations
                # Complexity: Minimum length, use of both letters and numbers, special characters
                if len(password) < 8:
                    messages.error(request, "Password must be at least 8 characters long.")
                    return redirect('uni_register')
                if not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password) or not re.search(r'[^A-Za-z0-9]', password):
                    messages.error(request, "Password must contain at least one letter, one number, and one special character.")
                    return redirect('uni_register')
                
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
                
                messages.success(request, "Registration successful. You can now log in.")
                return redirect('login')
            else:
                messages.error(request, "Please fill in vbvbvcall fields.")
        
        except Exception as e:
            messages.error(request, "")
            print(str(e))  # Print the exception details for debugging purposes
        
    else:
        form = RegistrationForm()
        university_form = UniversityPersonForm()
        
    return render(request, 'uni_register.html', {'form': form, 'university_form': university_form})




#outsider form

def outsider_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        outsider_form = OutsiderForm(request.POST)
        
        if form.is_valid() and outsider_form.is_valid():
            # Process the user registration form data
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            phone_number = form.cleaned_data['phone_number']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']
            role_id = form.cleaned_data['role_id'].role_id
            
            role = Role.objects.get(role_id=role_id)
            user = User(username=username, first_name=first_name, last_name=last_name,
                        date_of_birth=date_of_birth, phone_number=phone_number, gender=gender,
                        address=address, password=password, role=role)
            user.save()
            
            # Process the university person registration form data
            nic = outsider_form.cleaned_data['nic'] 
            outsider_person = Outsider(nic=nic, user_id=user)
            outsider_person.save()


    


            return redirect('login')
    else:
        form = RegistrationForm()
        outsider_form = OutsiderForm()

    return render(request, 'outsider_registration.html', {'form': form, 'outsider_form': outsider_form})




def admin(request):
    # Logic for admin page
    return render(request, 'admin.html')

def uniPerson(request):
    # Logic for university page
    return render(request, 'uniPerson.html')

def outsider(request):
    # Logic for outsider page
    return render(request, 'outsider.html')