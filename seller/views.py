from django.shortcuts import render,redirect
from .models import Product
from users.models import Customer

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
        return render(request,'myshop/orders.html')
    else:
        return redirect('login')

def test(request,shopdomain):
    prods = Product.objects.all().values()

    return render(request,'myshop/test.html',{'products':prods})