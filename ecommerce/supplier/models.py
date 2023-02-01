from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contactFirstName = models.CharField(max_length=50)
    contactLastName = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    # logo = 