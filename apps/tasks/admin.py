from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "project",
        "assigned_to",
        "priority",
        "status",
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "priority",
        "status",
        "project",
    )