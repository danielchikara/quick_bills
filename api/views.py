from rest_framework import status
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

#clase que crea el token cuando se inicia sesión


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


#clase que se utiliza para refrescar el token 
class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
    
# Registro de usuario
class UserRegirsterView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BillGetAndCreateView(APIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data) 
        if serializer.is_valid():
            serializer.save(client_bills = self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        queryset = self.queryset.filter(client_bills=self.request.user)
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductGetAndCreateView(APIView):
    queryset = Product.objects.filter(is_active = True)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def get(self, request, *args, **kwargs):
        queryset = self.queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)