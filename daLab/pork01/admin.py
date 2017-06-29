from django.contrib import admin

from .models import Suppliers, Products, Orders
#from .models import Suppliers, Products, Orders, ProductsAdmin, OrderAdmin

admin.site.register(Suppliers)
admin.site.register(Products) #Model must be declared before the AdminModel
admin.site.register(Orders) #Model must be declared before the AdminModel
#admin.site.register(Products, ProductsAdmin) #Model must be declared before the AdminModel
#admin.site.register(Orders, OrderAdmin) #Model must be declared before the AdminModel
