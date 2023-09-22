from django.db import models
from seller.models import Product
from users.models import Customer,Shop

class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)

    @property
    def total_cost(self):
        return self.product_qty * self.product.selling_price