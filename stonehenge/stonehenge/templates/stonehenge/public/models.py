from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    '''Custom user model'''
    is_staff = models.BooleanField(default=False)
