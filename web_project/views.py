from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'web_project/dashboard.html')

def product(request):
    return render(request, 'web_project/products.html')
def customer(request):
    return render(request, 'web_project/customers.html')