# apps/daily_logs/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField


# Local imports
from .models import Testing, Status, Prevision

# Create your serializers here

class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class PrevisionSerializer(ModelSerializer):
    class Meta:
        model = Prevision
        fields = '__all__'


class TestingSerializer(ModelSerializer):
    status = StatusSerializer(read_only=True) # PARA LECTURA
    status_id = PrimaryKeyRelatedField(
        source='status',
        queryset=Status.objects.all(),
        write_only=True
    ) # PARA ESCRITURA
    prevision = PrevisionSerializer(read_only=True) # PARA LECTURA
    prevision_id = PrimaryKeyRelatedField(
        source='prevision',
        queryset=Prevision.objects.all(),
        write_only=True
    ) # PARA ESCRITURA

    class Meta:
        model = Testing
        fields = '__all__'