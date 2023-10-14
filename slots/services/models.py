from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

class Service(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

