from django.contrib import admin

from .models import (
    Workspace,
    WorkspaceMember,
)
@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
        "is_active",
    )

    search_fields = (
        "name",
        "slug",
    )

    list_filter = (
        "is_active",
    )



@admin.register(WorkspaceMember)
class WorkspaceMemberAdmin(admin.ModelAdmin):

    list_display = (
        "workspace",
        "user",
        "joined_at",
    )

    search_fields = (
        "workspace__name",
        "user__email",
    )
