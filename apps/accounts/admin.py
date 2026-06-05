from django.contrib import admin

from apps.accounts.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        "employee_id",
        "email",
        "role",
        "is_active",
    )

    search_fields = (
        "employee_id",
        "email",
    )

    list_filter = (
        "role",
        "is_active",
    )
