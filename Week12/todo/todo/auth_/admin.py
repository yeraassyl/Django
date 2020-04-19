from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from todo.auth_.models import MyUser,Profile


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('id','username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )


@admin.register(Profile)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id','bio','address','user')
