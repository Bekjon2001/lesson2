from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _

from main.base import BaseMeta,BaseModel

class Account(AbstractBaseUser,BaseModel):
    """
    Associate with user account
    """
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer.'),
        error_messages={
            'unique': _(" Bu user nomi mavjud "),
        }
    )
    first_name = models.CharField(_("first_name"),max_length=30, blank=True)
    last_name = models.CharField(_("last_name"),max_length=150, blank=True)
    middle_name = models.CharField(_("middle_name"),max_length=150, blank=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "username"


    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """
        Returns True if the user has a specific permission.
        """
        return self.is_superuser

    def has_module_perms(self, app_label):
        """
        Returns True if the user has permissions for the given app.
        """
        return self.is_superuser

    class Meta(BaseMeta):
        verbose_name = _('user')
        verbose_name_plural = _('users')