from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

# Create your models here.

# Model to store user projects


class Project(models.Model):
    STATUS = (
        ('Inactive', 'Inactive'),
        ('Active', 'Active'),
        ('Completed', 'Completed'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="projects",
        on_delete=models.CASCADE,
        null=True,
    )
    deadline = models.DateTimeField(
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS,
        default='Inactive'
    )
    tags = TaggableManager()

    def __str__(self):
        return self.name
