from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # Replace with your model
from pms_app.models import *
class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ['email']  
    list_display = ['u_name', 'email', 'role','is_staff']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('u_name', 'email', 'role', 'password', 'is_staff', 'is_active'),
        }),
    )

admin.site.register(User, CustomUserAdmin)