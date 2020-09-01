from django.db import models

# User model is exist origianlly in django users management system
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    name = models.FloatField()

    # for checking shipping option
    digital = models.BooleanField(default=False, null=True, blank=False)
   
    def __str__(self):
        return self.name
    