from django.shortcuts import render,redirect
from users.models import Shop,Customer

def addcustomer(request):
    if request.method == 'POST':
        shop_id = request.session['shop']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        address_city = request.POST['address_city']
        address_state = request.POST['address_state']
        address_pin = request.POST['address_pin']

        
        shop = Shop.objects.get(shop_id = shop_id)
        password = "newcustomer@"+shop.shop_domain
        newcus = Customer(name = name, email = email, password = password, phone = phone, address = address, address_city = address_city, address_state = address_state, address_pin = address_pin, shop_id = shop)
        newcus.save()
    return redirect('addcustomer')