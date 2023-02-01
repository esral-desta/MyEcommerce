from django.db import models

# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=100,null=False,blank=False)
    LastName = models.CharField(max_length=300,null=False,blank=False)
    # profilePic = 
    address = models.IntegerField(null=False,blank=False)
    postalCode = models.IntegerField(null=False,blank=False)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName +" "+self.LastName