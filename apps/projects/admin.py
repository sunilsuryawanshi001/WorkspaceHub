from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "workspace",
        "status",
        "is_active",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "workspace",
        "status",
        "is_active",
    )