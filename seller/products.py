from django.shortcuts import render,redirect
from .models import Product
from users.models import Shop

def edit_product(request,shopdomain):
    product_id = request.POST['product_id']
    product = Product.objects.get(product_id = product_id)
    product.name = request.POST['name']
    product.description = request.POST['description']
    product.original_price = request.POST['original_price']
    product.selling_price = request.POST['selling_price']
    quantity = int(request.POST['quantity']) + int(request.POST['addstock'])
    product.quantity = quantity
    product.save()
    return redirect('products',shopdomain = shopdomain)

def add_product(request,shopdomain):
    name = request.POST['name']
    description = request.POST['description']
    original_price = request.POST['original_price']
    selling_price = request.POST['selling_price']
    quantity = request.POST['quantity']
    product_image = request.FILES['product_image']
    shop_id = request.session['shop']
    shop = Shop.objects.get(shop_id = shop_id)
    product = Product(name = name, description = description, original_price = original_price, selling_price = selling_price, quantity = quantity, product_image = product_image, shop_id = shop)
    product.save()
    return redirect('addproducts',shopdomain = shopdomain)
