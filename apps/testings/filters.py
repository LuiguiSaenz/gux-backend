from rest_framework import filters
from .models import Testing
from django_filters import rest_framework as filters

class CustomFilter(filters.FilterSet):

    class Meta:
        model = Testing
        fields = {
          'alta_date': ['lte', 'gte'],
          'rol': ['exact', 'contains'],
          'prevision': ['exact'],
          'status': ['exact'],
        }