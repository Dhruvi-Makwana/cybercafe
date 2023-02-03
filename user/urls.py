from django.urls import path
from .views import GetSystemData, UserData, RegisterSystem, User_register, SystemUpdate, UserUpdate, ManageHistory,AdminLogin,Add_System

app_name = 'user'
urlpatterns = [
    path('systems/', GetSystemData.as_view(), name='homepage'),
    path('show_user/', UserData.as_view(), name='showuser'),
    path('system_register/', RegisterSystem.as_view(), name='system-register'),
    path('user_register/', User_register.as_view(), name='user-register'),
    path('getdata/', GetSystemData.get_data, name='getdata'),
    path('get-userdata/', UserData.get_userdata, name='getuserdata'),
    path('system_update/<pk>/', SystemUpdate.as_view(), name="system_update"),
    path('user_update/<pk>/', UserUpdate.as_view(), name="system_update"),
    path('assign_system', ManageHistory.as_view(), name="assign_system"),
    path('login', AdminLogin.as_view(), name='login'),
    path('add_system', Add_System.as_view(),name='addsystem')
]
