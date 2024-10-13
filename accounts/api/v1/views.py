from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializer import UserSerializer,RegistrationSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class ProfileAPIView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


    def get(self,request,format=None):
        user = self.request.user
        data = get_object_or_404(User,id=user.id)
        serializer = self.get_serializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class RegistrationAPIView(GenericAPIView):
    serializer_class = RegistrationSerializer


    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        username = serializer._validated_data['username']
        user = User.objects.get(username=username)
        token, created = Token.objects.get_or_create(user=user)
        serializer.save()
        return Response({"user":username,"token":token.key,'message':"successfully registered"},status=status.HTTP_201_CREATED)
    

    
    

    