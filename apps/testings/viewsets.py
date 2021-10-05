# apps/daily_logs/viewsets.py
# Python imports

# Django imports

# Third party apps imports
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Local imports
from .serializers import TestingSerializer, StatusSerializer, PrevisionSerializer
from .models import Testing, Status, Prevision
from .filters import CustomFilter


class TestingViewSet(ModelViewSet):
    serializer_class = TestingSerializer
    queryset = Testing.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_class = CustomFilter
    search_fields = ('patient',)

    class Meta:
        model = Testing
        fields = '__all__'


class StatusViewSet(ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    class Meta:
        model = Status
        fields = '__all__'


class PrevisionViewSet(ModelViewSet):
    serializer_class = PrevisionSerializer
    queryset = Prevision.objects.all()

    class Meta:
        model = Prevision
        fields = '__all__'
