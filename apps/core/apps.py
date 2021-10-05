# apps/core/apps.py
# Python imports


# Django imports
from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


# Third party apps imports


# Local imports


# Configure your app here.
class CoreConfig(AppConfig):
    name = 'apps.core'
    verbose_name = 'Iscontrolapi'


class CoreAdminConfig(AdminConfig):
    default_site = 'apps.core.admin.ISAdminSite'
