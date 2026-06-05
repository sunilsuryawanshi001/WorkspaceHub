from django.contrib import admin

from .models import Workspace

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
