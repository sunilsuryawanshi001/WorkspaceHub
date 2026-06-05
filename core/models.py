import uuid

from django.db import models

class BaseModel(models.Model):
    """
    Base model inherited by all business models.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    created_at = models.DateField(
        auto_now_add=True
    )

    updated_at = models.DateField(
        auto_now=True
    )

    is_deleted = models.BooleanField(
        default=False
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        abstract = True