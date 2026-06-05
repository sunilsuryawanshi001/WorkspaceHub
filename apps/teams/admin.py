from django.contrib import admin

from .models import (
    Team,
    TeamMember,
)


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


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):

    list_display = (
        "team",
        "user",
        "is_team_lead",
        "joined_at",
    )

    search_fields = (
        "team__name",
        "user__email",
    )

    list_filter = (
        "is_team_lead",
        "team",
    )