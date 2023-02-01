from django.db import models

# Create your models here.
class Order(models.Model):
    # customerId =
    # productId =
    orderDate = models.DateTimeField(auto_now_add=True)
    tax = models.IntegerField()
    paid = models.BooleanField(default=False)