from rest_framework import serializers
from .models import Temperature

class TemperatureSerializes(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ["name"]
