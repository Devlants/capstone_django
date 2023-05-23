from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import Category1Serializer, Category2Serializer

from .models import Category1, Category2

class category1ListView(ListAPIView):
    queryset = Category1.objects.all()
    serializer_class = Category1Serializer

class category2ListView(ListAPIView):
    serializer_class = Category2Serializer

    def get_queryset(self):
        parent = Category1.objects.get(id = self.kwargs["id"])
        return Category2.objects.filter(parent = parent)

