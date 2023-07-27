from rest_framework import serializers
from .models import Menu
from category.models import Category1

class MenuEasySerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ["id","image","name","price"]

class MenuCateSerializer(serializers.ModelSerializer):
    menues = MenuEasySerializer(many=True)
    class Meta:
        model = Category1
        fields = ["name","menues"]




