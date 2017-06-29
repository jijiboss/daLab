from django.contrib import admin

#from .models import Suppliers, Products, Orders
from .models import Suppliers, Products, Orders, ProductsAdmin, OrdersAdmin

admin.site.register(Suppliers)
#admin.site.register(Products) #Model must be declared before the AdminModel
#admin.site.register(Orders) #Model must be declared before the AdminModel
admin.site.register(Products, ProductsAdmin) #Actual model must be declared before the AdminModel
admin.site.register(Orders, OrdersAdmin) #Actual model must be declared before the AdminModel
