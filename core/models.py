import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    pk = models.UUIDField(
        _('id'),
        name='id',
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    class Meta:
        abstract = True
