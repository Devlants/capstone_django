from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializers import MenuEasySerializer, MenuCateSerializer, MenuIDSerializer
from rest_framework.response import Response
from .models import Menu
from category.models import Category1, Category2

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class MenuListView(ListAPIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       return super(MenuListView, self).dispatch(request, *args, **kwargs)

    queryset = Category1.objects.filter(id__gte = '3')
    serializer_class = MenuCateSerializer

class MenuEasyListView(ListAPIView):
    serializer_class = MenuEasySerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       return super(MenuEasyListView, self).dispatch(request, *args, **kwargs)
    def get_queryset(self):
        category = Category2.objects.get(id = self.kwargs["id"])
        return Menu.objects.filter(category_2 = category)

class MenuAPIView(APIView):
    def get(self,request):
        data = MenuIDSerializer(Menu.objects.all(),many = True).data
        return Response(data)

