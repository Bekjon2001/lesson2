import uuid
from django.db import models
from django.conf import settings



class BaseModel(models.Model):
    """
    Barcha odellar uchun assosiy Base model
    """
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='%(class)s_created_by'

    )

    class Meta:
        abstract = True

class BaseMeta(object):
    ordering = ('-created_at',)