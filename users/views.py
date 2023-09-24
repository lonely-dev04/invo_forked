from django.shortcuts import render,redirect
from . models import Shop,Customer
from django.contrib import messages
from django.db import IntegrityError
from django.utils import timezone


def shop_login(request):
    if 'shop' not in request.session:

        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            user = Shop.objects.filter(email=email, password=password).first()
            
            if user is not None:
                request.session['shop'] = user.shop_id
                request.session['owner_name'] = user.owner_name
                request.session['shopdomain'] = user.shop_domain
                user.last_login = timezone.now()
                messages.success(request, 'Successfully logged in.')
                response = redirect("dashboard", shopdomain = request.session['shopdomain'])
                return response
            else:
                messages.error(request, 'Wrong email or password')

        return render(request,'users/shop-login.html')
    else:
        messages.warning(request, 'Already logged in')
        return redirect("dashboard", shopdomain = request.session['shopdomain'])

def shop_register(request):
    if request.method == 'POST':
        try:
            shop_name = request.POST['shop_name']
            owner_name = request.POST['owner_name']
            email = request.POST['email']
            password = request.POST['password']
            shop_domain = request.POST['domain']
            shop_domain = shop_domain.replace(" ","")
            shop_domain = shop_domain.replace("invo.in/","")
            phone = request.POST['phone']
            address = request.POST['address']
            address_city = request.POST['address_city']
            address_state = request.POST['address_state']
            address_pin = request.POST['address_pin']

            new_shop = Shop(shop_name = shop_name, owner_name = owner_name, email = email, password = password, shop_domain = shop_domain, phone = phone, address = address, address_city = address_city, address_state = address_state, address_pin = address_pin)
            new_shop.save()
            cash_sale = Customer(name = "Cash Sale",email = "cashsale."+shop_domain+"@invo.in", password = "cashsale@invo", shop_id = new_shop)
            cash_sale.save()
            messages.success(request, 'Registration success. You can login in now')
            return redirect('login')
        except IntegrityError as e:
            if 'email' in str(e):
                messages.error(request,'E-mail already exists')
            if 'shop_domain' in str(e):
                messages.error(request,'Shop Domain already exists')
            return redirect('register')
    return render(request,'users/shop-register.html')

def shop_logout(request):
    if 'shop' in request.session:
        del request.session['shop']
        del request.session['owner_name']
        del request.session['shopdomain']
        messages.info(request, 'Logged out successfully')
        response = redirect('login')
        return response
    return redirect('login')

def customer_login(request):
    if 'customer' not in request.session:

        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            user = Customer.objects.filter(email=email, password=password).first()
            
            if user is not None:
                request.session['customer'] = user.customer_id
                request.session['customer_name'] = user.name.split()[0]
                return redirect("index")
            else:
                messages.warning(request,'Wrong email or password')


        return render(request,'users/customer-login.html',{'login':'login'})
    return redirect("index")

def customer_logout(request):
    if 'customer' in request.session:
        del request.session['customer']
        if 'customer_name' in request.session:
            del request.session['customer_name']
        if 'current_shop' in request.session:
            del request.session['current_shop']
        if 'current_shopdomain' in request.session:
            del request.session['current_shopdomain']
        response = redirect('index')
        return response
    else:
        messages.info(request, 'Not logged in yet')
        return redirect('customer_login')

def customer_register(request):

    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            phone = request.POST['phone']
            address = request.POST['address']
            address_city = request.POST['address_city']
            address_state = request.POST['address_state']
            address_pin = request.POST['address_pin']

            new_customer = Customer(name = name, email = email, password = password, phone = phone, address = address, address_city = address_city, address_state = address_state, address_pin = address_pin)
            new_customer.save()
            messages.success(request, 'Registration Successful. Login to continue')
            return redirect('customer_login')
        except IntegrityError as e:
            if 'email' in str(e):
                messages.error(request,'E-mail already exists')
            return redirect('customer_register')


    return render(request,'users/customer-register.html',{'register':'register'})