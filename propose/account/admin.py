from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
	model = User

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
