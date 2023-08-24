from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response

@permission_classes((AllowAny,))
class SignalAPIView(APIView):
    def get(self,request):
        return Response(getattr(settings,"SIGNAL"))

    def post(self,request):
        print(request.data["signal"][0])
        if request.data["signal"][0] == 1:
            settings.SIGNAL = True
        else:
            settings.SIGNAL = False
        print(settings.SIGNAL)
        return Response(status=200)


