from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","is_active"]
    

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255,write_only=True)

    class Meta:
        model=User
        fields = ["username","password",'password1']

    def validate(self, attrs):
        if attrs.get('password')!=attrs.get('password1'):
            raise serializers.ValidationError({'detail':'Password does not match'})
        
        try:
            validate_password(attrs.get('password'))
        except ValidationError as error:
            raise serializers.ValidationError({'password':list(error.messages)})
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('password1',None)
        return User.objects.create_user(**validated_data)
    

class TokenDecodeSerializer(serializers.Serializer):
    pass