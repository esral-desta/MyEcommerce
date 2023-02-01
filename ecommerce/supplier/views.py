from django.shortcuts import render
from .models import Supplier
from .forms import SupplierForm
# Create your views here.

def createSupplier(request):

    form = SupplierForm()

    context ={
        "form":form
    }
    return render(request, "supplier/create.html",context)

def allSuppliers(request):
    context ={
        
    }
    return render(request, "supplier/list.html",context)

def detailSupplier(request,id):
    context ={
        
    }
    return render(request, "supplier/detail.html",context)

def updateSupplier(request,id):

    form = SupplierForm()

    context ={
        "form":form
    }
    return render(request, "supplier/create.html",context)

def deleteSupplier(request,id):
    context ={
        
    }
    return render(request, "supplier/delete.html",context)