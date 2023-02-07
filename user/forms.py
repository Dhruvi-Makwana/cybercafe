from django import forms

from .choice import AVAILABLE
from .models import System,ConfigureSystems,User,System_User_Histories
from django.contrib.auth.forms import AuthenticationForm


from .choice import AVAILABLE
from .models import System,ConfigureSystems,User,System_User_Histories
from django.contrib.auth.forms import AuthenticationForm



class Register_System(forms.ModelForm):
    class Meta:
        model = ConfigureSystems
        fields = ['name', 'company', 'ram', 'unit']


class User_Register(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','password','email','mobile_number']

class Register_System(forms.ModelForm):
    class Meta:
        model = ConfigureSystems
        fields = ['name', 'company', 'ram', 'unit']


class User_Register(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'email', 'mobile_number']


class AssignSystem(forms.ModelForm):
    # system_user = forms.ModelChoiceField(queryset=User.objects.all())
    # system = forms.ModelChoiceField(queryset=System.objects.filter(status=AVAILABLE))
    class Meta:
        model = System_User_Histories
        fields = ['system_user', 'system', 'assign_time', 'finish_time']

    # def __init__(self, *args,**kwargs):
    #     super(AssignSystem, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].required = False


class AdminLoginForm(AuthenticationForm):
    pass


class AddSystem(forms.ModelForm):
    class Meta:
        model = System
        fields = ['name', 'status']
