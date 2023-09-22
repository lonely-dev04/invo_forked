from django.contrib import admin
from . models import Product,Order,OrderDetails

admin.site.register(Product)
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderDetails)
