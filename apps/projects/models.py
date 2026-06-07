from django.db import models

from core.models import BaseModel
from core.constants import ProjectStatus
from apps.workspaces.models import Workspace

from django.conf import settings


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
    

class ProjectMember(BaseModel):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="members"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="project_membership"
    )

    is_project_lead = models.BooleanField(
        default=False
    )

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "project_members"
        unique_together = (
            ("project", "user")
        )

    def __str__(self):
        return (
            f"{self.user.email} - "
            f"{self.project.name}"
        )