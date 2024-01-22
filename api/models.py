from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

"""modelo cliente que reutiliza el modelo de django de usuario y se modifica para que pueda iniciar sesion con correo 
"""
class Client(AbstractUser):
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
    document = models.CharField(max_length=20)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length= 500)
    
    def __str__(self) -> str:
        return self.email


class Bill(models.Model):
    client_bills = models.ForeignKey(Client, related_name = "bills_client", on_delete=models.CASCADE)
    company_name = models.CharField( max_length=50)
    nit = models.CharField( max_length=50)
    code = models.CharField(max_length=1)
    
    def __str__(self) -> str:
        return self.client_bills.first_name


class Product (models.Model):
    name =models.CharField( max_length=50)
    description = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name    


class Bills_Products(models.Model):
    bills_fk = models.ForeignKey(Bill, related_name="product_bills", on_delete=models.CASCADE)
    product_fk = models.ForeignKey(Product, related_name="product_bills", on_delete=models.CASCADE) 
    
    def __str__(self) -> str:
        return f"client_document, {self.client_fk.document}, product_name, {self.product.name}"
    
