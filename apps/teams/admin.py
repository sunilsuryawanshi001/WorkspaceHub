from django.contrib import admin

from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "workspace",
        "is_active",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "workspace",
        "is_active",
    )