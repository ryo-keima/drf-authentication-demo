from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        user.full_clean()

        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email=email,
            username=username,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(
            email=email,
            username=username,
            password=password,
            **extra_fields,
        )


class User(AbstractBaseUser):

    username = models.CharField(
        verbose_name=_("username"),
        unique=True,
        max_length=150
    )
    email = models.EmailField(
        verbose_name=_("Email Address"),
        unique=True
    )
    age = models.IntegerField(
        verbose_name=_("age"),
    )

    objects = UserManager()

    def __str__(self):
        return self.username
