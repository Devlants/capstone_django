from rest_framework import serializers
from .models import Temperature, Size


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ["name"]

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["name"]
