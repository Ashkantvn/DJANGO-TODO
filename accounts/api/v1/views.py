from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer,RegistrationSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


class ProfileAPIView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


    def get(self,request,format=None):
        user = self.request.user
        data = get_object_or_404(User,id=user.id)
        serializer = self.get_serializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class TokenProfileAPIView(ProfileAPIView):
    def get(self, request,token, format=None):
        user = Token.objects.get(key=token).user
        serializer = self.get_serializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


# token base views
class RegistrationAPIView(GenericAPIView):
    serializer_class = RegistrationSerializer


    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user": serializer.data["username"],
                "token": token.key,
                'message': "successfully registered"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginAPIView(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({"user":user.username,'token': token.key})
    


class LogoutAPIView(APIView):
    
    def get(self, request,token,format=None):
        try:
            result = get_object_or_404(Token, key=token)
            result.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    
    

