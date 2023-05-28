from django.shortcuts import render, redirect
from django.contrib.auth import logout
from apps.product_view.models import Product,ActiveOrder
from django.contrib.auth.decorators import login_required
import json
from django.contrib import messages
def check(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('alogin')

def log_out(request):
    logout(request)
    return redirect('home')

class Main_view:
    @login_required(login_url="alogin")
    def deshboard(request):
        products = Product.objects.all()
        con = {
            'products' : products
        }
        return render(request, 'dashboard.html', con)
        
    @login_required(login_url="alogin")
    def manage(request):
        if request.method == "POST":
            item = Product.objects.get(item_name= request.POST['item_name'])
            if request.POST['select'] == "Add":
                 
                item.available += int(request.POST['amount'])
                item.total_amount += int(request.POST['amount'])
                messages.add_message(request, messages.INFO, f"{request.POST['amount']} {item.item_name}'s add successfuly ")

            else:
                if int(request.POST['amount'])<= item.available:
                    item.available -= int(request.POST['amount'])
                    item.total_amount -= int(request.POST['amount'])
                    messages.add_message(request, messages.INFO, f"{request.POST['amount']} {item.item_name}'s removed successfuly ")
                else:
                    messages.add_message(request, messages.WARNING, "Not Enough Items, Check the amount and submit again.")


            item.save()
        items = Product.objects.values_list('item_name', flat=True)
        items_amount = Product.objects.values_list('available', flat=True)
        json_data = json.dumps(list(items))
        json_data_availble = json.dumps(list(items_amount))
        return render(request, 'manage.html',{
            'items': json_data,
            'availble' : json_data_availble,
            })

    @login_required(login_url="alogin")
    def add(request):
        if request.method == "POST":
            new_item = Product()
            new_item.item_name = request.POST['product_name']
            new_item.total_amount = request.POST['total_amount']
            new_item.on_order = request.POST['on_order']
            new_item.available = int(request.POST['total_amount']) - int(request.POST['on_order'])
            new_item.save()
            messages.add_message(request, messages.INFO, f"{new_item.item_name} add successfuly ")

        return render(request, 'add.html',)
    @login_required(login_url="alogin")
    def activeOrders(request):
        data = ActiveOrder.objects.all()
        
        return render(request, 'activeorder.html', {'orders' : data})
    
    @login_required(login_url="alogin")
    def order(request):
        if request.method == "POST":
            
            data = json.loads(request.POST['add_data'])
            for i in data:

                my_object = Product.objects.get(item_name=i[0])
                my_object.available -= int(i[1])
                my_object.on_order += int(i[1])
                my_object.save()
            new = ActiveOrder()
            new.order_name = request.POST['name']
            new.order_location = request.POST['address']
            new.contact = request.POST['contact']
            new.order_data = data
            new.save()
            messages.add_message(request, messages.INFO, "Order sucsessfully created")
        items = Product.objects.values_list('item_name', flat=True)
        items_amount = Product.objects.values_list('available', flat=True)
        json_data = json.dumps(list(items))
        json_data_availble = json.dumps(list(items_amount))
        return render(request, 'order.html', {
            'items': json_data,
            'availble' : json_data_availble,
            }) 
    @login_required(login_url="alogin")
    def order_complete(request, slug):
        order = ActiveOrder.objects.get(order_id=slug)
        order_details = eval(order.order_data)
        for i in order_details:
            item = Product.objects.get(item_name=i[0])
            item.available += int(i[1])
            item.on_order -= int(i[1])
            item.save()
        messages.add_message(request, messages.INFO, f"Order of {order.order_name} completed successfully.")
        order.delete()
        
        return redirect('dashboard')