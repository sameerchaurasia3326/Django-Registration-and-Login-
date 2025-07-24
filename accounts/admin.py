
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_filter = ('is_superuser', 'is_staff', 'is_active')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register your models here.
