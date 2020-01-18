from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import customuser


class CustomUserAdmin(UserAdmin):
    # add_form =
    # form =
    model = customuser
    list_display = ["username", "email", "is_staff"]


admin.site.register(customuser, CustomUserAdmin)