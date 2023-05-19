from datetime import timezone
import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.db import models
from .models import Item,Flavours, Toppings,  Amount, Option, Coverage, Shape, Order, User, OrderItem

from django.http import HttpResponse
# Create your views here.
def home (request):
    return render(request, 'Cupcakaya/index.html')



def Cupcakes (request):
    context = {
        'cup_flavours' : Flavours.objects.filter(category='Cup'), 
        'toppings' :Toppings.objects.filter(category='Cup'), 
        'amountt' : Amount.objects.filter(category='Cup')

    }

    if request.method == 'POST':
        itemflav_id = request.POST['flavors']
        itemflav = Flavours.objects.get(flav_id=itemflav_id)

        itemtop_id = request.POST['toppingbtn']
        itemtop = Toppings.objects.get(top_id=itemtop_id)

        itemamo_id = request.POST['amountbtn']
        itemamo = Amount.objects.get(amo_id=itemamo_id)
        price = 100 + itemtop.price + itemamo.price + itemflav.price
        cat = 'Cup'
        image = 'static/Cupcakaya/cupcakes.jpg'
        new_item = Item.objects.create(flavour = itemflav, topping=itemtop, amount=itemamo, category = cat,price=price, image=image)
        new_item.save()
        new_orderitem = OrderItem.objects.create(item=new_item)
        new_orderitem.save()
        new_order = Order.objects.create()
        
        new_order.items.add(new_orderitem)
        
    return render(request, 'Cupcakaya/Cupcakes.html',context)
    







def Cakes (request):
    context = {
        'cake_flavours' : Flavours.objects.filter(category='Ck'), 
        'options' :Option.objects.filter(category='Ck'),
        'coveragee' : Coverage.objects.filter(category='Ck')

    }


    if request.method == 'POST':
        itemflav_id = request.POST['flavors']
        itemflav = Flavours.objects.get(flav_id=itemflav_id)

        itemcov_id = request.POST['coveragebtn']
        itemcov = Coverage.objects.get(cove_id=itemcov_id)

        itemop_id = request.POST['optionbtn']
        itemop = Option.objects.get(opt_id=itemop_id)
        price = 100 + itemcov.price + itemop.price + itemflav.price
        cat = 'Ck'
        image = 'static/Cupcakaya/cakes.jpg'
        new_item = Item.objects.create(flavour = itemflav, coverage= itemcov, option=itemop, category = cat, price=price, image=image)
        new_item.save()
        new_orderitem = OrderItem.objects.create(item=new_item)
        new_orderitem.save()
        new_order = Order.objects.create()
        new_order.items.add(new_orderitem)
        
    return render(request, 'Cupcakaya/Cakes.html',context)
    

def Cookies (request):
    context = {
        'cookie_flavours' : Flavours.objects.filter(category='Co'), 
        'shapes' : Shape.objects.filter(category='Co'), 
        'amountt' : Amount.objects.filter(category='Co')

    }

    if request.method == 'POST':
        itemflav_id = request.POST['flavors']
        itemflav = Flavours.objects.get(flav_id=itemflav_id)

        itemshape_id = request.POST['shapebtn']
        itemshape = Shape.objects.get(shape_id=itemshape_id)

        itemamo_id = request.POST['amountbtn']
        itemamo = Amount.objects.get(amo_id=itemamo_id)

        price = 100 + itemshape.price + itemamo.price + itemflav.price
        cat = 'Co'
        image = 'static/Cupcakaya/cookies.jpg'
        new_item = Item.objects.create(flavour = itemflav, shape=itemshape, amount=itemamo, category = cat, price = price, image=image)
        new_item.save()
        new_orderitem = OrderItem.objects.create(item=new_item)
        new_orderitem.save()
        new_order = Order.objects.create()
        new_order.items.add(new_orderitem)
        
    
   
    return render(request, 'Cupcakaya/Cookies.html', context)





def Cakepops (request):
    context = {
        'pop_flavours' : Flavours.objects.filter(category='Cp'),  
        'coveragee' :Coverage.objects.filter(category='Cp'),
        'amountt' : Amount.objects.filter(category='Cp')

    }
    if request.method == 'POST':
        itemflav_id = request.POST['flavors']
        itemflav = Flavours.objects.get(flav_id=itemflav_id)

        itemcov_id = request.POST['coveragebtn']
        itemcov = Coverage.objects.get(cove_id=itemcov_id)

        itemamo_id = request.POST['amountbtn']
        itemamo = Amount.objects.get(amo_id=itemamo_id)
        price = 100 + itemcov.price + itemamo.price + itemflav.price
        cat = 'Cp'
        image = 'static/Cupcakaya/cakepops.jpg'
        new_item = Item.objects.create(flavour = itemflav, coverage= itemcov, amount=itemamo, category = cat, price=price, image=image)
        new_item.save()
        new_orderitem = OrderItem.objects.create(item=new_item)
        new_order = Order.objects.create()

        new_order.items.add(new_orderitem)
        
        new_order.save()
        
        
        
    return render(request, 'Cupcakaya/cakepops.html',context)

def cart (request):

    context = {
        'in_items': Item.objects.all()
    }
    if request.method == 'POST':

        itemslug = request.POST['btnslug']
        item = Item.objects.get(slug=itemslug)

        item.delete()
        
    return render(request, 'Cupcakaya/cart.html', context)

def faq (request):
    return render(request, 'Cupcakaya/faq.html')

def about (request):
    return render(request, 'Cupcakaya/about.html')

def form (request):

    if request.method == 'POST':

        usernameunique = request.POST['1username']
        username = request.POST['firstname']
        userlast = request.POST['lastname']
        usernum = request.POST['number']       
        usercountry = request.POST['country']
        useraddr = request.POST['address']
        usercomment = request.POST['subject']

        new_user = User.objects.create( username= usernameunique, name=username, lname=userlast, number=usernum, country=usercountry, address=useraddr, comment=usercomment)
        new_user.save()
        ordered = True
        order_date = datetime.datetime.now()
        
        

        new_order = Order.objects.create(user=new_user, ordered_date= order_date, ordered=ordered)
        new_order.save()
        
    return render(request, 'Cupcakaya/form.html')

def Menu(request):
    context = {
        'items' : Item.objects.all()
    }
    return render(request, "Cupcakaya/Menu.html", context)








