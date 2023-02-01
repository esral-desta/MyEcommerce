from django.urls import path
from . import views
app_name = "supplier"
urlpatterns =[
    path("",views.allSuppliers,name="all"),
    path("create",views.createSupplier,name="create"),
    path("detail/<int:id>",views.detailSupplier,name="detail"),
    path("update/<int:id>",views.updateSupplier,name="update"),
    path("delete/<int:id>",views.deleteSupplier,name="delete"),
]