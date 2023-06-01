from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializers import MenuEasySerializer, MenuCateSerializer

from .models import Menu
from category.models import Category1, Category2

class MenuListView(ListAPIView):
    queryset = Category1.objects.filter(id__gte = '3')
    serializer_class = MenuCateSerializer

class MenuEasyListView(ListAPIView):
    serializer_class = MenuEasySerializer

    def get_queryset(self):
        category = Category2.objects.get(id = self.kwargs["id"])
        return Menu.objects.filter(category_2 = category)


