from django.shortcuts import render,redirect
from django.http import JsonResponse
from users.models import Shop, Customer
from seller.models import Product,Order,OrderDetails
from . models import Cart
import json
from django.contrib import messages

# Create your views here.
def ui(request):
    return render(request, "home/ui.html")

def index(request):
    return render(request, 'home/index.html',{'active_page': 'home'})

def shop(request):
    if request.method == 'POST':
        state = request.POST['state']
        city = request.POST['city']
        if state != '0' and city != '0':
            shops = Shop.objects.filter(address_city=city,address_state=state)
            return render(request,'home/shop.html',{'active_page': 'shop','shops':shops})
        else:
            messages.warning(request,'Select your State and City')
        

    address_data = Shop.objects.values('address_state', 'address_city')
    address_dict = {}

    for entry in address_data:
        address_state = entry['address_state']
        address_city = entry['address_city']
        if address_state in address_dict:
            if address_city not in address_dict[address_state]:
                address_dict[address_state].append(address_city)
        else:
            address_dict[address_state] = [address_city]

    return render(request,'home/shop.html',{'active_page': 'shop','address':address_dict})

def gotoshop(request, shopdomain):
    shop = Shop.objects.filter(shop_domain = shopdomain).first()
    
    if shop:
        shop_id = shop.shop_id
        products = Product.objects.filter(shop_id = shop_id)
        request.session['current_shop'] = shop_id
        request.session['current_shopdomain'] = shop.shop_domain
        return render(request,'home/shop.html',{'active_page': 'shop','products':products,'shopname':shop.shop_name})
    else:
        return redirect('shop')


def cart(request, shopdomain):
    shop = Shop.objects.filter(shop_domain = shopdomain).first()
    if request.method == 'POST':
        print("post executes")
        customer_id = request.session['customer']
        customer = Customer.objects.get(customer_id = customer_id)
        items = Cart.objects.filter(shop = shop, customer = customer)
        for item in items:
            name = 'qty'+str(item.id)
            item.product_qty = int(request.POST[name])
            item.save()
    if shop is not None:
        if 'customer' not in request.session:
            return redirect('customer_login')
        shop_id = shop.shop_id
        request.session['current_shop'] = shop_id
        request.session['current_shopdomain'] = shop.shop_domain
        customer_id = request.session['customer']
        customer = Customer.objects.get(customer_id = customer_id)

        items = Cart.objects.filter(shop = shop, customer = customer)
        return render(request, 'home/cart.html',{'products': items})
    else:
        return redirect('shop')
    
    
    
def checkout(request, shopdomain):
    if 'current_shop' in request.session:
        shop = Shop.objects.filter(shop_domain = shopdomain).first()
        if shop is not None:
            if 'customer' not in request.session:
                return redirect('customer_login')
            customer_id = request.session['customer']
            customer = Customer.objects.get(customer_id = customer_id)

            items = Cart.objects.filter(shop = shop, customer = customer)
            return render(request, 'home/checkout.html',{'products': items})
        else:
            return redirect('cart',shopdomain = request.session['current_shopdomain'])
    else:
        redirect('shop')
    

def addtocart(request,shopdomain):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        shop = Shop.objects.filter(shop_domain = shopdomain).first()
        if shop is not None:
            if 'customer' in request.session:
                data=json.load(request)
                product_id=data['pid']
                customer_id = request.session['customer']
                customer = Customer.objects.get(customer_id = customer_id)

                product = Product.objects.get(product_id = product_id)
                if product:
                    if Cart.objects.filter(customer = customer,product =product):
                        return JsonResponse({'status':'Product Already in Cart'}, status=200)
                    else:
                        if product.quantity>=1:
                            
                            Cart.objects.create(customer = customer,product =product, product_qty=1,shop = shop)
                            return JsonResponse({'status':'Product Added to Cart'}, status=200)
                        else:
                            return JsonResponse({'status':'Product Stock Not Available'}, status=200)
            else:
                return JsonResponse({'status':'Login to Add Cart'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)
    
    
def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("cart",shopdomain = request.session['current_shopdomain'])

def create_order(request, shopdomain):
    shop = Shop.objects.filter(shop_domain = shopdomain).first()
    customer = Customer.objects.get(customer_id = request.session['customer'])
    items = Cart.objects.filter(shop = shop, customer = customer)
    order_value = 0
    paid = 0
    for item in items:
        order_value += item.total_cost


    address = str(customer.address)+","+str(customer.address_city)+","+str(customer.address_state)+"-"+str(customer.address_pin)
    order = Order(customer = customer, shop_id = shop, order_value = order_value, shipping_address = address, paid = paid, order_mode = 1,completed = 0)
    order.save()
    for item in items:
        prod = item.product
        quantity = item.product_qty
        price = item.product.selling_price
        total = item.total_cost
        orderdetails = OrderDetails(order = order, product = prod, quantity = quantity, price = price, total_price = total)
        orderdetails.save()

    for item in items:
        item.delete()

    return redirect('thankyou', shopdomain = request.session['current_shopdomain'])

def thankyou(request, shopdomain):
    return render(request, 'home/thankyou.html')

def myorders(request, shopdomain):
    if 'customer' in request.session:
        shop = Shop.objects.get(shop_domain=shopdomain)
        customer_id = request.session['customer']
        customer = Customer.objects.get(customer_id=customer_id)
        orders = Order.objects.filter(customer=customer, shop_id=shop)
        orderdetails = []

        for order in orders:
            order_details = OrderDetails.objects.filter(order=order)
            orderdetails.append({'order': order, 'details': order_details})

        return render(request, 'home/myorders.html', {'orderdetails': orderdetails})
    else:
        return redirect('shop')