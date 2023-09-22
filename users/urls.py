from django.urls import path
from . import views

urlpatterns = [
    path('shop/login',views.shop_login, name='login'),
    path('shop/register',views.shop_register, name='register'),
    path('shop/logout',views.shop_logout, name='logout'),
    path('customer/login',views.customer_login, name='customer_login'),
    path('customer/logout',views.customer_logout, name='customer_logout'),
    path('customer/register',views.customer_register, name='customer_register')
]