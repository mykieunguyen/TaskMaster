from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    avatar = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )

    # def __str__(self):
    #     return self.user
