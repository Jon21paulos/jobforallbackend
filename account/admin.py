from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    pass

# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Jobseeker)