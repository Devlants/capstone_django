from rest_framework import serializers
from .models import Temperature, Size,Option

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ["name"]

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["name"]

class OptionSerializer(serializers.ModelSerializer):
    menu = serializers.CharField(source = "menu.name")
    temperature = serializers.CharField(source = "temperature.name")
    size = serializers.CharField(source = "size.name")
    class Meta:
        model = Option
        fields = ["menu", "temperature","size"]
