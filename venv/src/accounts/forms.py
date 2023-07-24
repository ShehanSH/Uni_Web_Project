
from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm,PasswordResetForm
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Role, Faculty, Department, UniStudent
from django import forms
from .models import UniStudent, UniStaff, Outsider


class CustomRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'abc', 'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'abc', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'abc', 'placeholder': 'Last Name'}))
    date_of_birth = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'class': 'abc', 'placeholder': 'YYYY-MM-DD'}))
    phone_number = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(attrs={'class': 'abc', 'placeholder': 'Phone Number'}))
    gender = forms.ChoiceField(label='Gender', choices=[('male', 'Male'), ('female', 'Female')], widget=forms.Select(attrs={'class': 'abc'}))
    address = forms.CharField(label='Address', widget=forms.Textarea(attrs={'class': 'abc', 'placeholder': 'Address'}))
    password1 = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput(attrs={'class': 'abc', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password', max_length=255, widget=forms.PasswordInput(attrs={'class': 'abc', 'placeholder': 'Confirm Password'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'abc', 'placeholder': 'Email'}))
    # role = forms.ModelChoiceField(queryset=Role.objects.all())
    role = forms.ModelChoiceField(queryset=Role.objects.all(), widget=forms.Select(attrs={'class': 'abc'}))
    

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'date_of_birth', 'phone_number', 'gender', 'address', 'email', 'password1', 'password2', 'role')


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'abc', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'abc', 'placeholder': 'Password'}))



class UniStudentRegstrationForm(forms.ModelForm):
    student_id = forms.CharField(label='Student ID', max_length=255, widget=forms.TextInput(attrs={'class': 'abc', 'placeholder': '_ _ _ _/_ _ _ _/_ _ _'}))
    class Meta:
        model = UniStudent
        fields = ('student_id', 'faculty', 'department')
        widgets = {
            'faculty': forms.Select(attrs={'class': 'abc'}),
            'department': forms.Select(attrs={'class': 'abc'}),
        }
    

class UniStaffRegstrationForm(forms.ModelForm):
    staff_id = forms.CharField(label='Staff ID', max_length=255, widget=forms.TextInput(attrs={'class': 'abc', 'placeholder': '_ _ _ _/_ _ _ _/_ _ _'}))
   
    class Meta:
        model = UniStaff
        fields = ('staff_id', 'faculty', 'department')
        widgets = {
            'faculty': forms.Select(attrs={'class': 'abc'}),
            'department': forms.Select(attrs={'class': 'abc'}),
        }
    

class OutsiderRegstrationForm(forms.ModelForm):
    
    class Meta:
        model = Outsider
        fields = ('nic',)
        widgets = {
            'nic': forms.TextInput(attrs={'class': 'abc'}),
        }

from django.contrib.auth.forms import SetPasswordForm

class SetPasswordForm(SetPasswordForm):
    
    class Meta:
        model = CustomUser
        fields = ('password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'abc'}),
            'password2': forms.PasswordInput(attrs={'class': 'abc'}),
        }

class PasswordResetForm(PasswordResetForm):
        
        class Meta:
            model = CustomUser
            fields = ('password1', 'password2')
            widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'abc'}),
            'password2': forms.PasswordInput(attrs={'class': 'abc'}),
        }