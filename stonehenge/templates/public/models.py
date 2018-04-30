from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    '''Custom user model'''
    profile_picture = models.ImageField(blank=True, null=True)

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def __str__(self):
        if self.first_name and self.last_name:
            return "{0} {1}".format(self.first_name, self.last_name)
        else:
            return self.email
