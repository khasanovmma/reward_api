from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {"fields": ("coins",)},
        ),
    )
    list_display = ("username", "email", "coins", "is_staff")
