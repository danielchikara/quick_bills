from django.shortcuts import render
from .serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#clase que crea el token cuando se inicia sesión
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


#clase que se utiliza para refrescar el token 
class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer