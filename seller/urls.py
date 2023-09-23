from django.urls import path
from . import views,products,billing,customers

urlpatterns = [
    path('ui',views.ui, name='ui'),
    path('',views.dashboard, name="dashboard"),
    path('products',views.products, name="products"),
    path('customers',views.customers, name="customers"),
    path('addproducts',views.addproducts, name="addproducts"),  
    path('addcustomer',views.addcustomer, name="addcustomer"),    
    path('bill',views.billing,name="billing"),
    path('sales',views.sales,name="sales"),
    path('orders',views.orders,name="orders"),
    path('order_completed/<str:oid>',views.order_completed, name = "order_completed"),
    path('edit_product',products.edit_product, name='edit_product'),
    path('add_product',products.add_product,name='add_product'),
    path('add_customer',customers.addcustomer,name='add_customer'),
    path('create_bill',billing.create_bill,name='create_bill'),
    path('delete_product/<str:pid>',products.delete_product, name='delete_product'),
]