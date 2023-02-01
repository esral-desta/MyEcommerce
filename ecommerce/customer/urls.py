from django.urls import path
from . import views
app_name= "customer"
urlpatterns =[
    path("",views.allCustomer,name="all"),
    path("create",views.createCustomer,name="create"),
    path("detail/<int:id>",views.detailCustomer,name="detail"),
    path("update/<int:id>",views.updateCustomer,name="update"),
    path("delete/<int:id>",views.deleteCustomer,name="delete"),
]