from django.shortcuts import render
from .models import Order
from .forms import OrderForm
# Create your views here.

def createOrder(request):

    form = OrderForm()

    context ={
        "form":form
    }
    return render(request, "order/create.html",context)

def allOrders(request):
    context ={
        
    }
    return render(request, "order/list.html",context)

def detailOrder(request,id):
    context ={
        
    }
    return render(request, "order/detail.html",context)

def updateOrder(request,id):

    form = OrderForm()

    context ={
        "form":form
    }
    return render(request, "order/create.html",context)

def deleteOrder(request,id):
    context ={
        
    }
    return render(request, "order/delete.html",context)