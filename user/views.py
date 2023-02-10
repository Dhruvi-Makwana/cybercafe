import json

from django.shortcuts import render,get_object_or_404
from pip._internal.cli import status_codes

from .choice import AVAILABLE
from .models import System, User, System_User_Histories,ConfigureSystems
from django.http import JsonResponse
from django.db.models import Value
from django.db.models import CharField
from django.db.models.functions import Concat
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.views import (
    LoginView,
   )
from django.views.generic import ListView, CreateView, UpdateView
from .forms import Register_System, User_Register, AssignSystem, AdminLoginForm, AddSystem
from django.views.generic.edit import ModelFormMixin, ProcessFormView


class GetSystemData(CreateView, MultipleObjectMixin, ModelFormMixin):
    template_name = "user/homepage.html"
    model = System_User_Histories, ConfigureSystems, System
    form_class = AssignSystem
    object_list = System.objects.values('id', 'name__id', 'name__name', 'name__company', 'name__ram', 'name__unit', 'status')

    def post(self, request, *args, **kwargs):

        obj = get_object_or_404(System, id=request.POST.get("id"))

        obj.name = request.POST.get("name__name")
        obj.company = request.POST.get("name__company")
        obj.ram = request.POST.get("name__ram")
        obj.unit = request.POST.get("name__unit")
        obj.status = request.POST.get("status")
        obj.save()
        # set


        register_system = Register_System(request.POST)
        if register_system.is_valid():
            System.objects.create(name= register_system.save(), status=AVAILABLE)
            return render(request, "user/register_System.html", {"register_system": register_system})

        getdata = json.loads(request.body)
        user = getdata.get('users')
        get_list_system = getdata.get('systems')
        s_time = getdata.get('start_time')
        e_time = getdata.get('finish_time')
        data_dict = {"system_user_id": user, "assign_time": s_time, "finish_time": e_time}


        def createdata(system):
            data_dict.update({"system_id": system})
            return System_User_Histories(**data_dict)

        result = list(map(createdata, get_list_system))
        System_User_Histories.objects.bulk_create(result)
        return render(request, "user/homepage.html", {"assign_system": getdata})

    def get_user(request):
        user_data = User.objects.annotate(
            full_name=Concat('id', Value(' '), 'first_name', Value(' '), 'last_name', Value(' ('), ('email'),
                             Value(') '), output_field=CharField())).values('id', 'full_name')
        return JsonResponse({'data': list(user_data)}, safe=False)


class UserData(ListView):
    template_name = "user/display_user_details.html"
    model = User
    users = User.objects.all()

    def get_queryset(self):
        data = User.objects.values('id', 'first_name', 'last_name', 'mobile_number')
        return data


class RegisterSystem(CreateView):

    form_class = Register_System
    success_url = '/homepage/'

    def get(self, request, *args, **kwargs):
        return render(request, "user/register_System.html", {"register_system": Register_System()})

    def post(self, request, *args, **kwargs):

        register_system = Register_System(request.POST)
        if register_system.is_valid():
            register_system.save()

        return render(request, "user/register_System.html", {"register_system": register_system})


class User_register(CreateView):
    form_class = User_Register

    def get(self, request, *args, **kwargs):
        return render(request, "user/user_register.html", {"user_register": User_Register()})

    def post(self, request, *args, **kwargs):

        save_user = User_Register(request.POST)
        if save_user.is_valid():

            adduser = save_user.save()
            adduser.set_password(adduser.password)
            save_user.save()

        return render(request, "user/user_register.html", {"user_register": save_user})


class SystemUpdate(UpdateView):
    success_url = "../../systems"
    model = ConfigureSystems
    fields = ['name', 'company', 'ram', 'unit']
    template_name = "user/system_update.html"


class UserUpdate(UpdateView):
    success_url = "../../showuser/"
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = "user/user_update.html"


class AdminLogin(LoginView):
    template_name = 'user/admin_login.html'
    authentication_form = AdminLoginForm


class Add_System(CreateView):

    form_class = AddSystem
    success_url = '/homepage/'

    def get(self, request, *args, **kwargs):
        return render(request, "user/add_system.html", {"add_system": AddSystem()})

    def post(self, request, *args, **kwargs):

        add_system = AddSystem(request.POST)
        if add_system.is_valid():
            add_system.save()

        return render(request, "user/add_system.html", {"add_system": add_system})


class System_assign_listing(ListView):
    model = System_User_Histories
    template_name = "user/system_listing.html"
    context_object_name = 'system_list'

    def get_queryset(self):
        return System_User_Histories.objects.all()