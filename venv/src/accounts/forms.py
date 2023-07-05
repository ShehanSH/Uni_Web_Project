from django import forms
from .models import Role, User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Role, Faculty, Department

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=255, error_messages={'required': 'Fields cannot be empty.'})
    password = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput, error_messages={'required': 'Fields cannot be empty.'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'username',
            'password',
            Submit('submit', 'Login')
        )

class CustomSelectWidget(forms.Select):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'abc'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)


# class RegistrationForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=255, widget=forms.TextInput(attrs={'class': 'abc'}))
#     password = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput(attrs={'class': 'abc'}))

#     #role = forms.ModelChoiceField(label='Role', queryset=Role.objects.filter(role_name__in=['Admin', 'University Person', 'Outsider']))
#     role = forms.ModelChoiceField(
#         label='Role',
#         queryset=Role.objects.filter(role_name__in=['Admin', 'University Person', 'Outsider']),
#         widget=CustomSelectWidget()
#     )

#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError('Username already exists')
#         return username



from django import forms


from .models import Role, Faculty, Department
from django import forms
from .models import Role

class RoleSelectionForm(forms.Form):
    role_id = forms.ModelChoiceField(label='Role', queryset=Role.objects.all())


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=255, widget=forms.TextInput(attrs={'class': 'abc'}))
    first_name = forms.CharField(label='First Name', max_length=255, widget=forms.TextInput(attrs={'class': 'abc'}))
    last_name = forms.CharField(label='Last Name', max_length=255, widget=forms.TextInput(attrs={'class': 'abc'}))
    email = forms.EmailField(label='Email', max_length=255, widget=forms.EmailInput(attrs={'class': 'abc'}))
    date_of_birth = forms.DateField(label='Date of Birth', required=False, widget=forms.DateInput(attrs={'class': 'abc'}), input_formats=['%Y-%m-%d'])
    phone_number = forms.CharField(label='Phone Number', max_length=20, widget=forms.TextInput(attrs={'class': 'abc'}))
    gender = forms.ChoiceField(label='Gender', choices=[('male', 'Male'), ('female', 'Female')], widget=forms.Select(attrs={'class': 'abc'}))
    address = forms.CharField(label='Address', widget=forms.Textarea(attrs={'class': 'abc'}))
    password = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput(attrs={'class': 'abc'}))
    confirm_password = forms.CharField(label='Confirm Password', max_length=255, widget=forms.PasswordInput(attrs={'class': 'abc'}))
    role_id = forms.ModelChoiceField(label='Role', queryset=Role.objects.all(), widget=forms.Select(attrs={'class': 'abc'}))


class UniversityPersonForm(forms.Form):
    
    student_id = forms.CharField(label='Student ID', max_length=255,widget=forms.TextInput(attrs={'class': 'abc'}))
    faculty_id = forms.ChoiceField(label='Faculty', widget=forms.Select(attrs={'class': 'abc'}))
    department_id = forms.ChoiceField(label='Department', widget=forms.Select(attrs={'class': 'abc'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['faculty_id'].choices = self.get_faculty_choices()
        self.fields['department_id'].choices = self.get_department_choices()

    def get_faculty_choices(self):
        faculties = Faculty.objects.all()
        choices = [(faculty.faculty_id, faculty.faculty_name) for faculty in faculties]
        return choices

    def get_department_choices(self):
        departments = Department.objects.all()
        choices = [(department.department_id, department.department_name) for department in departments]
        return choices


class OutsiderForm(forms.Form):
    nic = forms.CharField(label='NIC', max_length=255)

