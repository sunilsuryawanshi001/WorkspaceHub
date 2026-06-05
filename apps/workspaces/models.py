from django.db import models

from core.models import BaseModel

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