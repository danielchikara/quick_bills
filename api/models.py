from django.db import models

# Create your models here.

class Clients(models.Model):
    document = models.CharField(max_length=20)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length= 500)
    
    def __str__(self) -> str:
        return self.document

class Bill(models.Model):
    client_bills = models.ForeignKey(Clients, related_name = "bills_client", on_delete=models.CASCADE)
    company_name = models.CharField( max_length=50)
    nit = models.CharField( max_length=50)
    code = models.CharField(max_length=1)
    
    def __str__(self) -> str:
        return self.client_bills.first_name

class Bills_Products(models.Model):
    client_fk = models.ForeignKey(Clients, related_name="client_bills", on_delete=models.CASCADE)
