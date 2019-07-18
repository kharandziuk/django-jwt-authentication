from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils.translation import ugettext


class BaseModel(models.Model):
    # all models should be inheritted from this model
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, BaseModel):
    username = models.CharField(
        ugettext('Username'), max_length=255,
        db_index=True, unique=True
    )
    email = models.EmailField(
        ugettext('Email'), max_length=255, db_index=True,
        blank=True, null=True, unique=True
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email', 'password',)

    class Meta:
        app_label = 'users'
