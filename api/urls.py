from django.urls import path
from .views import *

urlpatterns = [
    # Your URLs...
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegirsterView.as_view(), name='user_regiter'),
    path('bill/',BillGetAndCreateView.as_view(), name="bill_create"),
    path('product/',ProductGetAndCreateView.as_view(), name="product_create"),
    path('bill/product/',BillProductView.as_view(), name="bill_product"),
    
]