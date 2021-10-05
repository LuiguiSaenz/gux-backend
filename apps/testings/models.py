# apps/daily_logs/models.py
# Python imports
from datetime import datetime, timedelta


# Django imports
from django.db import models


# Third party apps imports


# Local imports

# Create your models here.
class Prevision(models.Model):
    name = models.CharField(
        max_length=250
    )

    def __str__(self):
        return str(self.name)


class Status(models.Model):
    name = models.CharField(
        max_length=250
    )

    def __str__(self):
        return str(self.name)


class Testing(models.Model):
    rol = models.CharField(
        max_length=250
    )
    patient = models.CharField(
        max_length=250
    )
    hospital_date = models.DateField()
    alta_date = models.DateField()
    prevision_date = models.DateField()
    action = models.CharField(
        max_length=250
    )
    number = models.CharField(
        max_length=250
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )
    prevision = models.ForeignKey(
        Prevision,
        on_delete=models.CASCADE
    )
    pam = models.CharField(
        max_length=250
    )

    def __str__(self):
        return str(self.id)
        
    class Meta:
        ordering = ('id',)
