from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.user.managers import CustomUserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    name = models.CharField(_("name"), max_length=100)
    passage_id = models.CharField(max_length=255, unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set'  # Use um related_name diferente
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set'  # Use um related_name diferente
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]
