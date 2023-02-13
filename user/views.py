import json

from django.shortcuts import render
from user.choice import OCCUPIED

from django.urls import reverse_lazy
from .choice import AVAILABLE
from .models import System, User, System_User_Histories, ConfigureSystems
from django.http import JsonResponse
from django.db.models import Value
from django.db.models import CharField
from django.db.models.functions import Concat
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.views import (
    LoginView,LogoutView
)

from django.shortcuts import redirect, reverse
from django.views.generic import ListView, CreateView, UpdateView, View
from .forms import Register_System, User_Register, AssignSystem, AdminLoginForm, AddSystem
from django.views.generic.edit import ModelFormMixin, ProcessFormView


class GetSystemData(CreateView):
    template_name = "user/homepage.html"
    model = System
    form_class = AssignSystem

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = System.objects.values('id', 'name__id', 'name__name', 'name__company', 'name__ram',
                                                       'name__unit', 'status')
        return context

    def post(self, request, *args, **kwargs):
        if kwargs.get('operation')== 'create':
            register_system = Register_System(request.POST)
            if register_system.is_valid():
                System.objects.create(name=register_system.save(), status=AVAILABLE)
                return render(request, "user/register_System.html", {"register_system": register_system})

        # Assign system
            getdata = json.loads(request.body)
            user = getdata.get('users')
            get_list_system = getdata.get('systems')
            s_time = getdata.get('start_time')
            e_time = getdata.get('finish_time')
            data_dict = {"system_user_id": user, "assign_time": s_time, "finish_time": e_time}

            # breakpoint()

            System.objects.filter(id__in=get_list_system).update(status=OCCUPIED)

            def createdata(system):
                data_dict.update({"system_id": system})
                return System_User_Histories(**data_dict)

            result = list(map(createdata, get_list_system))
            System_User_Histories.objects.bulk_create(result)
            return render(request, "user/homepage.html", {"assign_system": getdata})

        # udate data code
        elif kwargs.get('operation') == 'update':
            getid = request.POST.get('id')
            update_data = System.objects.get(pk=getid)
            sys_name = request.POST.get('name__name')
            company_name = request.POST.get('name__company')
            ram = request.POST.get('name__ram')
            unit = request.POST.get('name__unit')
            status = request.POST.get('status')
            update_data.name.name = sys_name
            update_data.name.company = company_name
            update_data.name.ram = int(ram)
            update_data.name.unit = unit
            update_data.status = status
            update_data.name.save()
            update_data.save()

    def get_user(request):
        user_data = User.objects.annotate(
            full_name=Concat('id', Value(' '), 'first_name', Value(' '), 'last_name', Value(' ('), 'email',
                             Value(') '), output_field=CharField())).values('id', 'full_name')
        return JsonResponse({'data': list(user_data)}, safe=False)


class UserData(ListView):
    template_name = "user/display_user_details.html"
    model = User

    # users = User.objects.all()

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
    success_url = reverse_lazy('user:showuser')

    def get(self, request, *args, **kwargs):
        return render(request, "user/user_register.html", {"user_register": User_Register()})

    def post(self, request, *args, **kwargs):
        save_user = User_Register(request.POST)
        if save_user.is_valid():
            adduser = save_user.save()
            adduser.set_password(adduser.password)
            save_user.save()
            return redirect(reverse('user:showuser'))
        return render(request, "user/user_register.html", {"user_register": save_user})


class SystemUpdate(UpdateView):
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

    def get(self, request, *args, **kwargs):
        return render(request, "user/add_system.html", {"add_system": AddSystem()})

    def post(self, request, *args, **kwargs):
        add_system = AddSystem(request.POST)
        if add_system.is_valid():
            add_system.save()

        return render(request, "user/add_system.html", {"add_system": add_system})


class System_assign_listing(ListView):
    model = System_User_Histories
    template_name = "user/assign_system_list.html"
    context_object_name = 'system_list'

    def get_queryset(self):
        return System_User_Histories.objects.all().order_by('-id')
