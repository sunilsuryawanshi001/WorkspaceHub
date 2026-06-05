from django.db import models

from core.models import BaseModel
from apps.workspaces.models import Workspace

from django.conf import settings


class Team(BaseModel):

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name="teams"
    )

    name = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = "teams"
        ordering = ["name"]
        unique_together = (
            ("workspace", "name"),
        )

    def __str__(self):
        return self.name
    


class TeamMember(BaseModel):

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="members"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="team_memberships"
    )

    is_team_lead = models.BooleanField(
        default=False
    )

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "team_members"
        unique_together = (
            ("team", "user"),
        )

    def __str__(self):
        return (
            f"{self.user.email} - "
            f"{self.team.name}"
        )