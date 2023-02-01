from django.shortcuts import render,redirect
from .models import Customer
from .forms import CustomerForm
# Create your views here.

def createCustomer(request):

    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('/')
        else:
            print(form.errors)
    context ={
        "form":form
    }
    return render(request, "customer/create.html",context)

def allCustomer(request):
    customers = Customer.objects.all()
    context ={
        "customers":customers
    }
    return render(request, "customer/list.html",context)

def detailCustomer(request,id):
    customer = Customer.objects.get(id=id)

    context ={
        "customer" :  customer    
    }
    return render(request, "customer/detail.html",context)

def updateCustomer(request,id):

    customer = Customer.objects.get(pk=id)    
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
    context ={
        "form":form
    }
    return render(request, "customer/create.html",context)

def deleteCustomer(request,id):
    customer = Customer.objects.get(pk=id)
    if request.method == "POST":
        customer.delete()
        return redirect("/customer")
    context ={
        "customer" : customer        
    }
    return render(request, "customer/delete.html",context)