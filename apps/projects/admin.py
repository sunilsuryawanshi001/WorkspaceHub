from django.contrib import admin

from .models import (
    Project,
    ProjectMember,
)


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

@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "user",
        "is_project_lead",
        "joined_at",
    )

    search_fields = (
        "project__name",
        "user__email",
    )

    list_filter = (
        "project",
        "is_project_lead",
    )