

# Create your tests here.
from django.urls import path

from .views import GetSystemData, UserData, User_register, SystemUpdate, UserUpdate, Add_System, System_assign_listing

app_name = 'user'
urlpatterns = [
    path('systems/<str:operation>/', GetSystemData.as_view(), name='homepage'),
    path('show_user/', UserData.as_view(), name='showuser'),
    path('assign_system_list/', System_assign_listing.as_view(), name='assign_system_listing'),
    path('user_register/', User_register.as_view(), name='user_register'),
    # path('systems/<pk>/', SystemUpdate.as_view(), name="system_update"),
    path('user_update/<pk>/', UserUpdate.as_view(), name="user_update"),
    path('get_user/', GetSystemData.get_user, name="getuser"),
    path('add_system/', Add_System.as_view(), name='addsystem'),
]
