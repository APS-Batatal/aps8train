from django.utils import timezone
from django.db import models


# Create your models here.
class Line(models.Model):
    number = models.IntegerField()
    color = models.CharField(
        max_length=45
    )
    name = models.CharField(
        max_length=100
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )


class Log(models.Model):
    line = models.ForeignKey(
        Line,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    description = models.CharField(
        max_length=1000,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

