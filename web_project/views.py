from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders, 'total_customers': total_customers}
    return render(request, 'web_project/dashboard.html', context)

def product(request):
    drinks = Drink.objects.all()
    food = Food.objects.all()
    fruits = Fruit.objects.all()
    products = Product.objects.all()

    context = {'drinks': drinks, 'food': food, 'fruits': fruits, 'products': products}

    return render(request, 'web_project/products.html', context)

def customer(request):
    return render(request, 'web_project/customers.html')

def createOrder(request):

    form = OrderForm()  
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        # print('Printing POST', request.POST)


    context = {'form': form}

    return render(request, 'web_project/order_form.html', context)