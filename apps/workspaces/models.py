from django.db import models

from core.models import BaseModel

from django.conf import settings

class Workspace(BaseModel):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    slug = models.SlugField(
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = "workspaces"
        ordering = ["name"]

    def __str__(self):
        return self.name
    


class WorkspaceMember(BaseModel):

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name="members"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="workspace_memberships"
    )

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "workspace_members"
        unique_together = (
            ("workspace","user"),
        )

    def __str__(self):
        return (
            f"{self.user.email} - "
            f"{self.workspace.name}"
        )