from django.db import models

from core.models import BaseModel
from core.constants import ProjectStatus
from apps.workspaces.models import Workspace


class Project(BaseModel):

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    name = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=ProjectStatus.choices,
        default=ProjectStatus.PLANNING
    )

    start_date = models.DateField(
        null=True,
        blank=True
    )

    end_date = models.DateField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = "projects"
        ordering = ["name"]
        unique_together = (
            ("workspace", "name"),
        )

    def __str__(self):
        return self.name