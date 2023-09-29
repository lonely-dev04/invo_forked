from django.shortcuts import render,redirect
from users.models import Shop,Customer
from django.contrib.auth.hashers import check_password, make_password

def addcustomer(request,shopdomain):
    if request.method == 'POST':
        shop_id = request.session['shop']
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        address_city = request.POST['address_city']
        address_state = request.POST['address_state']
        address_pin = request.POST['address_pin']

        
        shop = Shop.objects.get(shop_id = shop_id)
        password = "newcustomer"
        try:
            newcus = Customer(name = name, email = email, password = make_password(password), phone = phone, address = address, address_city = address_city, address_state = address_state, address_pin = address_pin)
            newcus.save()
            newcus.shop_id.add(shop)
            newcus.save()
        except:
            customer = Customer.objects.get(email = email)
            customer.shop_id.add(shop)
            customer.save()
    return redirect('addcustomer',shopdomain = shopdomain)