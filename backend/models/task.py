from django.db import models
from django_extensions.db.models import TimeStampedModel


class Task(TimeStampedModel):
    title           = models.CharField(max_length=255, verbose_name="Title")
    description     = models.TextField(verbose_name="Task Description")
    completed       = models.BooleanField(default=False, verbose_name="Task Completed")

    def __str__(self):
        return self.title
