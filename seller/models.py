from django.db import models
import datetime
import os
from users.models import Shop,Customer

def getFileName(requset,filename):
    filename = filename.replace(" ","");  
    now_time=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('product_images/',new_filename)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True,default=None)
    name = models.CharField(max_length=100)
    description = models.TextField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    product_image = models.FileField(upload_to=getFileName)
    shop_id = models.ForeignKey(Shop,on_delete=models.CASCADE)
    status = models.BooleanField(default=False,help_text="0-Show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True,default=None)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    order_time = models.TimeField(auto_now_add=True)
    order_value = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()
    paid = models.BooleanField(default=True,help_text="0-unpaid 1-paid")
    order_mode = models.BooleanField(help_text="0-offline 1-online")
    completed = models.BooleanField(help_text='0-pending, 1-completed')

class OrderDetails(models.Model):
    id = models.AutoField(primary_key=True,default=None)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
