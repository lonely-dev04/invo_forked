from django.urls import path
from . import views

urlpatterns = [
    path("ui", views.ui, name="ui"),
    path("", views.index, name="index"),
    path("shop",views.shop,name="shop"),
    path("<str:shopdomain>/cart", views.cart, name= "cart"),
    path("<str:shopdomain>/checkout",views.checkout, name = "checkout"),
    path("<str:shopdomain>/",views.gotoshop , name="gotoshop"),
    path("<str:shopdomain>/addtocart", views.addtocart, name="addtocart"),
    path("<str:shopdomain>/createorder", views.create_order, name="create_order"),
    path("<str:shopdomain>/myorders",views.myorders, name = "myorders"),
    path("remove_cart/<str:cid>", views.remove_cart, name="remove_cart"),
    path("<str:shopdomain>/thankyou", views.thankyou, name = "thankyou"),
]