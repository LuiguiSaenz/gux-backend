# apps/daily_logs/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Testing, Status, Prevision


# Register your models here.
@admin.register(Testing)
class TestingModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Prevision)
class PrevisionModelAdmin(admin.ModelAdmin):
    pass
