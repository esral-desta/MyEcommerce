from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
# Create your views here.

def createProduct(request):

    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/product")
    context ={
        "form":form
    }
    return render(request, "product/create.html",context)

def allProducts(request):
    products = Product.objects.all()
    context ={
        "products":products
    }
    return render(request, "product/list.html",context)

def detailProduct(request,id):
    product = Product.objects.get(pk=id)
    context ={
        "product":product
    }
    return render(request, "product/detail.html",context)

def updateProduct(request,id):

    product = Product.objects.get(pk=id)
    form = ProductForm(instance = product)
    if request.method == "POST":
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("/product/detail/"+str(id))
    context ={
        "form":form
    }
    return render(request, "product/create.html",context)

def deleteProduct(request,id):
    product = Product.objects.get(pk=id)
    if request.method == "POST":
        product.delete()
        return redirect("/product")

    context ={
        "product":product
    }
    return render(request, "product/delete.html",context)