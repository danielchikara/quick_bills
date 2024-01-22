from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework import serializers
from .models import *

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username

        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        return super().validate(attrs)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Client
        fields  =["username","email","password"]
        extra_kwargs = {'password': {'write_only': True}}
        
        
    def create (self,validated_data):
        user = Client.objects.create_user(
            username=validated_data["username"],
            email= validated_data["email"],
            password=validated_data["password"]
            )
        return user
    

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill 
        exclude = ['client_bills','is_active']
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        exclude = ['is_active',]


class BillProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills_Products
        exclude = ['is_active',]