from django.urls import path
from . import views
app_name = 'order'
urlpatterns =[
    path("",views.allOrders,name="all"),
    path("create",views.createOrder,name="create"),
    path("detail/<int:id>",views.detailOrder,name="detail"),
    path("update/<int:id>",views.updateOrder,name="update"),
    path("delete/<int:id>",views.deleteOrder,name="delete"),
]