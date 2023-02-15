from django.contrib import admin

# Register your models here.
from .models import User, ConfigureSystems, System, System_User_Histories


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'mobile_number')


@admin.register(ConfigureSystems)
class ConfigureSystemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'purchase_date', 'ram', 'unit')
    list_per_page = 20


@admin.register(System)
class Systemadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    list_per_page = 20


@admin.register(System_User_Histories)
class System_User_HistoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'system_user', 'system', 'assign_time', 'finish_time')
