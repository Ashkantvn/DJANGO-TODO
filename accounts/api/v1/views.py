from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class TestAPIView(GenericAPIView):

    def get(self,request, format=None):
        return Response('OK')

    