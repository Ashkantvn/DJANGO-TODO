from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class ProfileAPIView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


    def get(self,request,format=None):
        user = self.request.user
        data = get_object_or_404(User,id=user.id)
        serializer = self.get_serializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    
    

    