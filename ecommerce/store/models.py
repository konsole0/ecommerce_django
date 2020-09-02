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
    price = models.FloatField()

    # for checking shipping option
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
   
    
    @property
    def imageUrl(self):
        # to prevent an error when the product doesn't have an image to render on the page
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name
    
class Order(models.Model):
    # 1-to-many relationship: customer can have multiple orders
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True) 
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=False, null=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True) 
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True) 
    quantity = models.IntegerField(default=0, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
