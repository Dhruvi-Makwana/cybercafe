from django import forms
from .models import System,ConfigureSystems,User,System_User_Histories
from django.contrib.auth.forms import AuthenticationForm


class Register_System(forms.ModelForm):
    class Meta:
        model = ConfigureSystems
        fields = ['name', 'company', 'ram', 'unit']


class User_Register(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'email', 'mobile_number']


class AssignSystem(forms.ModelForm):
    class Meta:
        model = System_User_Histories
        fields = ['system_user', 'system', 'assign_time', 'finish_time']


class AdminLoginForm(AuthenticationForm):
    pass


class AddSystem(forms.ModelForm):
    class Meta:
        model = System
        fields = ['name', 'status']
