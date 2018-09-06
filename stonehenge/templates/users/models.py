from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    '''Custom Auth User model'''
    full_name = models.CharField(max_length=256, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.full_name = self.first_name + self.last_name
        super(User, self).save(*args, **kwargs)
