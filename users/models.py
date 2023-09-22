from django.db import models

class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True,default=None)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_domain = models.CharField(max_length=20, unique=True)
    owner_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    address_city = models.CharField(max_length=50)
    address_state = models.CharField(max_length=50)
    address_pin = models.IntegerField()
    last_login = models.DateTimeField(null=True, blank=True)
    joined_in = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True,default=None)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    address_city = models.CharField(max_length=50)
    address_state = models.CharField(max_length=50)
    address_pin = models.IntegerField(null=True)
    joined_in = models.DateTimeField(auto_now_add=True)
    shop_id = models.ForeignKey(Shop,on_delete=models.CASCADE,null=True,blank=True)