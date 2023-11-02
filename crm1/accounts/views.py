from django.shortcuts import render
from django.http import HttpResponse,request
# Create your views here.

def Home(request):
    return render(request ,'accounts/dashboard.html',)

def Product(request):
    return render(request ,'accounts/product.html')

def Customer(request):
    return render(request , 'accounts/customer.html')
