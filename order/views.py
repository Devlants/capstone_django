import requests
from django.http import JsonResponse
from django.shortcuts import render
import json
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, Option, Temperature, Size
from menu.models import Menu
from .serializers import TemperatureSerializer, SizeSerializer, OptionSerializer
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

@csrf_exempt
def OrderCreateView(request):
    if request.method == "POST":
        access_token = request.META.get('HTTP_AUTHORIZATION')
        context = json.loads(request.body)
        total_price = 0
        order = Order.objects.create(is_pack = context["is_pack"],totalPrice=0)
        order.save()

        for data in context["data"]:
            option = Option()
            option.quantity = data["quantity"]
            menu = Menu.objects.get(name = data["name"])
            option.temperature = Temperature.objects.get(name = data["temperature"])
            option.size = Size.objects.get(name = data["size"])
            option.order = order
            option.menu = menu
            option.save()

            total_price += menu.price * option.quantity
        order.totalPrice = total_price
        order.save()
        options = order.option_set.all()
        options = OptionSerializer(options,many = True)
        print(options.data)
        data = {
            "brand" : "OKDK",
            "options" : options.data
        }
        header = {
            "Authorization" : access_token
        }
        api = getattr(settings,"APP_HOST")+"order/"
        response = requests.post(api,json = data,headers=header)
        print(response)
        return JsonResponse({"order_num":order.id})

class temperatureList(APIView):
    def get(self,request):
        temperatures = Temperature.objects.all()
        serializer = TemperatureSerializer(temperatures,many=True)

        return Response(serializer.data)

class SizeList(APIView):
    def get(self,request):
        sizes = Size.objects.all()
        serializer = SizeSerializer(sizes,many=True)

        return Response(serializer.data)
