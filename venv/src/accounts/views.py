from django.shortcuts import render, redirect
from .models import User
from .forms import RegistrationForm, LoginForm
from django.contrib import messages

from django.shortcuts import render, redirect
from .forms import RoleSelectionForm


from django.shortcuts import render, redirect
from .forms import RegistrationForm, UniversityPersonForm, OutsiderForm
from .models import User, UniversityPerson, Outsider, Role, Faculty, Department
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

    return render(request, 'role.html', {'form': form})

  


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






def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            phone_number = form.cleaned_data['phone_number']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            role_id = form.cleaned_data['role_id']

            role = Role.objects.get(role_name=role_id)
            user = User(username=username, first_name=first_name, last_name=last_name,
                        date_of_birth=date_of_birth, phone_number=phone_number, gender=gender,
                        address=address, password=password, confirm_password=confirm_password, role=role)
            user.save()

            if role_id == 'university_person':
                university_form = UniversityPersonForm(request.POST)
                if university_form.is_valid():
                    student_id = university_form.cleaned_data['student_id']
                    faculty_id = university_form.cleaned_data['faculty_id']
                    department_id = university_form.cleaned_data['department_id']

                    faculty = Faculty.objects.get(faculty_id=faculty_id)
                    department = Department.objects.get(department_id=department_id)

                    university_person = UniversityPerson(student_id=student_id, faculty=faculty, user=user,
                                                         department=department)
                    university_person.save()
            elif role_id == 'outsider':
                outsider_form = OutsiderForm(request.POST)
                if outsider_form.is_valid():
                    nic = outsider_form.cleaned_data['nic']

                    outsider = Outsider(nic=nic, user=user)
                    outsider.save()

            return redirect('login')
    else:
        form = RegistrationForm()
    
    return render(request, 'role.html', {'form': form})

def university_person_register(request):
    if request.method == 'POST':
        university_form = UniversityPersonForm(request.POST)
        if university_form.is_valid():
            student_id = university_form.cleaned_data['student_id']
            faculty_id = university_form.cleaned_data['faculty_id']
            department_id = university_form.cleaned_data['department_id']

            faculty = Faculty.objects.get(faculty_id=faculty_id)
            department = Department.objects.get(department_id=department_id)

            # Process the form data and save the university person details
            return redirect('login')
    else:
        university_form = UniversityPersonForm()

    return render(request, 'university_person_register.html', {'university_form': university_form})

def outsider_register(request):
    if request.method == 'POST':
        outsider_form = OutsiderForm(request.POST)
        if outsider_form.is_valid():
            nic = outsider_form.cleaned_data['nic']

            # Process the form data and save the outsider details
            return redirect('login')
    else:
        outsider_form = OutsiderForm()

    return render(request, 'outsider_register.html', {'outsider_form': outsider_form})




def admin(request):
    # Logic for admin page
    return render(request, 'admin.html')

def uniPerson(request):
    # Logic for university page
    return render(request, 'uniPerson.html')

def outsider(request):
    # Logic for outsider page
    return render(request, 'outsider.html')