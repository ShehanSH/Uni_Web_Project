from django import forms
from .models import Role, User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=255)
    password = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'username',
            'password',
            Submit('submit', 'Login')
        )


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=255)
    
    password = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput)

    role = forms.ModelChoiceField(label='Role', queryset=Role.objects.all())
    # role = forms.ModelChoiceField(label='Role', queryset=Role.objects.filter(role_name__in=['University Person', 'Outsider']))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username