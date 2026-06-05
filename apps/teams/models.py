from django.db import models

from core.models import BaseModel
from apps.workspaces.models import Workspace


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