from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Product,Order,OrderDetails
from users.models import Shop,Customer

@csrf_exempt
def create_bill(request,shopdomain):
    
    data = json.loads(request.body.decode('utf-8'))
    product_details = data.get('productDetails', [])
    customer = data.get('customer')
    billpaid = data.get('billpaid')
    
    shop_id = request.session['shop']

    customer = Customer.objects.get(customer_id = customer)
    shop = Shop.objects.get(shop_id = shop_id)


    bill_total = 0
    for product_data in product_details:
        total = product_data.get('total')
        bill_total+=total
    address = str(customer.address)+","+str(customer.address_city)+","+str(customer.address_state)+"-"+str(customer.address_pin)
    order = Order(customer = customer, shop_id = shop, order_value = bill_total, shipping_address = address, paid = billpaid, order_mode = 0,completed = 0)
    order.save()

    for product_data in product_details:
        product = product_data.get('product')
        quantity = product_data.get('quantity')
        price = product_data.get('price')
        total = product_data.get('total')
        prod = Product.objects.get(product_id = product)
        qty = prod.quantity
        qty -= quantity
        prod.quantity = qty
        prod.save()
        orderdetails = OrderDetails(order = order, product = prod, quantity = quantity, price = price, total_price = total)
        orderdetails.save()

    messages.success(request, 'Bill created Successfully')

    return redirect('billing',shopdomain = request.session['shopdomain'])