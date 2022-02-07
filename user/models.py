from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    CHOICES = (
        ('light.css', 'Light'),
        ('dark.css', 'Dark'),
    )

    language = models.CharField(max_length=10,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGE_CODE)
    theme = models.CharField(max_length=10,
                             choices=CHOICES,
                             default='light.css')
