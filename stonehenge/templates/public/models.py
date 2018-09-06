from django.contrib.auth.models import AbstractUser
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class User(AbstractUser):
    '''Custom Auth User model'''
    full_name = models.CharField(max_length=256, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.full_name = self.first_name + self.last_name
        super(User, self).save(*args, **kwargs)


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
    ]
