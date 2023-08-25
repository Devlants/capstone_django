from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response

@permission_classes((AllowAny,))
class SignalAPIView(APIView):
    SIGNAL = False
    def get(self,request):
        print(self.SIGNAL)
        return Response(self.SIGNAL)

    def post(self,request):
        if request.data["signal"][0] == "1":
            self.SIGNAL = True
        else:
            self.SIGNAL = False
        print(self.SIGNAL)
        return Response(status=200)


