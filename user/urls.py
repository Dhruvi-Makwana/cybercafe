from django.test import TestCase

# Create your tests here.
from django.urls import path
from .views import GetSystemData, UserData, RegisterSystem, User_register, SystemUpdate, UserUpdate,AdminLogin,Add_System,System_assign_listing

app_name = 'user'
urlpatterns = [
    path('systems/', GetSystemData.as_view(), name='homepage'),
    path('show_user/', UserData.as_view(), name='showuser'),
    path('listing/', System_assign_listing.as_view(), name='listing'),
    # path('system_register/', RegisterSystem.as_view(), name='system-register'),
    path('user_register/', User_register.as_view(), name='user-register'),
    path('systems/<pk>/', SystemUpdate.as_view(), name="system_update"),
    path('user_update/<pk>/', UserUpdate.as_view(), name="user_update"),
    # path('systems/', ManageHistory.as_view(), name="assign_system"),
    path('get_user/', GetSystemData.get_user, name="getuser"),
    path('add_system/', Add_System.as_view(), name='addsystem'),
]
