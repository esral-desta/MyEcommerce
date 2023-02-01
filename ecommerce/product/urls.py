from django.urls import path
from . import views

app_name= "product"

urlpatterns =[
    path("",views.allProducts,name="all"),
    path("create",views.createProduct,name="create"),
    path("detail/<int:id>",views.detailProduct,name="detail"),
    path("update/<int:id>",views.updateProduct,name="update"),
    path("delete/<int:id>",views.deleteProduct,name="delete"),
]