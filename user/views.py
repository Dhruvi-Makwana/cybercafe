from django.shortcuts import render
from .models import System, User
from django.http import JsonResponse
from django.db.models import F, Value, Func
from django.db.models import CharField
from django.db.models.functions import Concat
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.views import (
    LoginView,
   )
from django.views.generic import ListView, CreateView, UpdateView
from .forms import Register_System, User_Register, AssignSystem, AdminLoginForm, AddSystem


class GetSystemData(CreateView,MultipleObjectMixin):
    template_name = "user/homepage.html"
    model = User
    form_class = AssignSystem
    object_list = System.objects.values('id', 'name__name', 'name__company', 'name__ram', 'name__unit', 'status' )

    def post(self, request, *args, **kwargs):

        assign_system = request.POST.getlist('data')
        for getdata in assign_system:
            postdata_copy = request.POST.copy()
            postdata_copy['getdata'] = getdata
            add_history = AssignSystem(postdata_copy)
            if add_history.is_valid():
                add_history.save()
        return render(request, "user/homepage.html", {"assign_system": assign_system})

    # def get_queryset(self, *args, **kwargs):
    #     system_data = System.objects.values('id', 'name__name', 'name__company', 'name__ram', 'name__unit', 'status' )
    #
    #     return system_data

    def get_user(request):
        user_data = User.objects.annotate(full_name=Concat('id', Value(' '), 'first_name', Value(' '), 'last_name', Value(' ('), ('email'), Value(') '), output_field=CharField())).values('id','full_name')
        return JsonResponse({'data': list(user_data)}, safe=False)


class UserData(ListView):
    template_name = "user/display_user_details.html"
    model = User
    users = User.objects.all()

    def get_queryset(self):
        data = User.objects.values('id', 'first_name', 'last_name', 'mobile_number')
        return data
    # def get_userdata(self, request):
    #     getuser = []
    #     end = int(request.GET.get("length", 100))
    #     start = int(request.GET.get("start", 0))
    #     user_data = User.objects.all().values('id', 'first_name', 'last_name', 'mobile_number')
    #     user = User.objects.all()
    #     if getuser:
    #         filtered_user = user.filter(getuser__icontains=getuser)[start: end]
    #     else:
    #         filtered_user = user.filter()[start: end]
    #
    #     data = {
    #         "draw": 1,
    #         "recordsTotal": user.count(),
    #         "recordsFiltered": filtered_user.count(),
    #         "data": list(filtered_user.values('id', 'first_name', 'last_name', 'mobile_number'))
    #     }
    #
    #     return JsonResponse({'data': list(user_data)}, safe=False)
        # return JsonResponse({'data': list(user_data)}, safe=False)


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
    success_url = "../../homepage/"
    model = System
    fields = ['status']
    template_name = "user/system_update.html"


class UserUpdate(UpdateView):
    success_url = "../../showuser/"
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = "user/user_update.html"


# class ManageHistory(CreateView):
#     form_class = AssignSystem
#
#     def get(self, request, *args, **kwargs):
#         return render(request, "user/homepage.html", {"assign_system": AssignSystem()})
#
#     def post(self, request, *args, **kwargs):
#
#         assign_system = request.POST.getlist('data')
#         for getdata in assign_system:
#             postdata_copy = request.POST.copy()
#             postdata_copy['getdata'] = getdata
#             form2 = AssignSystem(postdata_copy)
#             if form2.is_valid():
#                 form2.save()


        # if assign_system.is_valid():
        #     assign_system.save()
        # return render(request, "user/homepage.html", {"assign_system": assign_system})


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
