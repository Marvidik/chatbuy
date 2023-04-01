from django.db import models 
from user.models import Vendor
from django.contrib.auth.models import User

# Create your models here.

choose=[
    ("men","men"),
    ("women","women"),
    ("supermarket","supermarket"),
    ("shoe","shoe"),
    ("bag","bag"),
    ("food","food"),
    ("watch","watch"),
    ("eletronic","eletronic"),
    ("phone","phone")
]

g_status=[
    ("Active","Active"),
    ("Disabled","Disabled")
]

class Products(models.Model):
    category=models.CharField(max_length=100,choices=choose)
    status=models.CharField(max_length=100,choices=g_status)
    name=models.CharField(max_length=100)
    sales=models.IntegerField()
    stock=models.IntegerField()
    price=models.IntegerField()
    store_name=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    image=models.ImageField()
    description=models.TextField()

    def __str__(self):

        return self.name



class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    store=models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name='carts')
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    ordered=models.BooleanField(default=False)
    date_ordered=models.DateTimeField(auto_now=True)


    def __str__(self):

        return self.user.username
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='orders')
    image=models.ImageField(null=True)
    name=models.CharField(max_length=100,null=True)
    quantity=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    shipping_address = models.TextField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} for {self.user.username}"


