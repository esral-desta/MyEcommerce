from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    # supplierID = 
    # categoryID = 
    unitPrice = models.IntegerField()
    # picture
    discount = models.IntegerField(null=True,blank=True)
    discountAvailable = models.BooleanField(default=False)