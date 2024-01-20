from django.db import models

# Create your models here.

class Client(models.Model):
    document = models.CharField(max_length=20)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length= 500)
    
    def __str__(self) -> str:
        return self.document


class Bill(models.Model):
    client_bills = models.ForeignKey(Client, related_name = "bills_client", on_delete=models.CASCADE)
    company_name = models.CharField( max_length=50)
    nit = models.CharField( max_length=50)
    code = models.CharField(max_length=1)
    
    def __str__(self) -> str:
        return self.client_bills.first_name


class Product ():
    name =models.CharField( max_length=50)
    description = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name    

class Bills_Products(models.Model):
    client_fk = models.ForeignKey(Client, related_name="client_bills", on_delete=models.CASCADE)
    product_fk = models.ForeignKey(Product, related_name="product_bills", on_delete=models.CASCADE) 
    
    def __str__(self) -> str:
        return f"client_document, {self.client_fk.document}, product_name, {self.product.name}"
    
