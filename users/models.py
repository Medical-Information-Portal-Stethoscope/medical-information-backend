from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

from core.models import TimeStampedMixin, UUIDMixin


class User(TimeStampedMixin, UUIDMixin, AbstractUser):
    """"
    Класс User представляет пользовательскую модель с дополнительным
    функционалом, таким как автоматическая генерация временных меток,
    добавление уникального идентификатора (UUID) и базовая реализация
    пользовательских атрибутов и методов.
    """
    class Meta:
        ordering = ['uuid']
        verbose_name = _('user')
        verbose_name_plural = _('users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    USER = 'user'
    MODER = 'moderator'
    ADMIN = 'admin'
    roles = [(USER, 'user'),
             (MODER, 'moderator'),
             (ADMIN, 'admin')]

    date_joined = None
    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(choices=roles,
                            default='user',
                            max_length=50)

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_moderator(self):
        return self.role == self.MODER

    @property
    def is_admin(self):
        return self.role == self.ADMIN
