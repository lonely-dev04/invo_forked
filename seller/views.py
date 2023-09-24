from django.shortcuts import render,redirect
from .models import Product,Order,OrderDetails
from users.models import Customer,Shop

def dashboard(request,shopdomain):
    if 'shop' in request.session:
        return render(request,'myshop/index.html')
    else:
        return redirect('login')

def ui(request):
    return render(request,'myshop/ui.html')

def products(request,shopdomain):
    if 'shop' in request.session:
        shop_id = request.session['shop']
        prods = Product.objects.filter(shop_id=shop_id)
        return render(request, 'myshop/products.html',{'products':prods})
    else:
        return redirect('login')
    
def customers(request,shopdomain):
    if 'shop' in request.session:
        shop_id = request.session['shop']
        name = "Cash Sale"
        custs = Customer.objects.filter(shop_id = shop_id).values()
        return render(request, 'myshop/customers.html',{'customers':custs})

def addproducts(request,shopdomain):
    return render(request,'myshop/addproducts.html')

def addcustomer(request,shopdomain):
    return render(request,"myshop/addcustomer.html")

def billing(request,shopdomain):
    if 'shop' in request.session:
        shop_id = request.session['shop']
        customers = Customer.objects.filter(shop_id = shop_id)
        products = Product.objects.filter(shop_id=shop_id)

        return render(request,'myshop/billing.html',{'customers' : customers, 'products' : products})    
    else:
        return redirect('login')
    

def sales(request,shopdomain):
    if 'shop' in request.session:
        return render(request,'myshop/sales.html')
    else:
        return redirect('login')

def orders(request,shopdomain):
    if 'shop' in request.session:
        shop_id = request.session['shop']
        orders = Order.objects.filter(shop_id = shop_id, order_mode=1, completed = 0)
        
        orderdetails = []

        for order in orders:
            order_details = OrderDetails.objects.filter(order=order)
            orderdetails.append({'order': order, 'details': order_details})

        return render(request, 'myshop/orders.html', {'orderdetails': orderdetails})
    else:
        return redirect('login')
    
def order_completed(request,shopdomain,oid):
    if 'shop' in request.session:
        order = Order.objects.get(order_id = oid)
        order.completed = 1
        order.save()
        return redirect('orders',shopdomain = shopdomain)
    else:
        return redirect('login')
