from django.db import models
from django.core.urlresolvers import reverse

#Supplier table
class Suppliers(models.Model):
    supplier = models.CharField(max_length=144)

    def __str__(self):
        return self.supplier

#Product table
class Products(models.Model):
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE) #Supplier
    prod_code_supplier = models.IntegerField(primary_key=True) #Supplier product code
    item_supplier = models.CharField(max_length=75) #Supplier Item Description
    prod_code_sumitomo = models.IntegerField() #Sumitomo product code
    item_sumitomo = models.CharField(max_length=75) #Sumitomo item description
    #is_favorite = models.BooleanField(default=False)

    #This method is called whenever a new Products entry has been created.
    #It will call "product_detail" passing pk ("kwargs" = "keyword args")
    #Basically it will load the product detail page for the new product just created
    def get_absolute_url(self):
        return reverse('1:product_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.supplier) + ' (' + str(self.prod_code_supplier) + ')' + ' - ' + self.item_supplier

#Order table
class Orders(models.Model):
    order_week = models.CharField(max_length=12)
    order_date = models.DateField()
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    prod_code_sumitomo = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_qty = models.IntegerField()
    fulfill_qty = models.IntegerField()
    production_date = models.DateField()
    trailer_num = models.CharField(max_length=25)
    port_of_loading = models.CharField(max_length=100)
    port_of_unlading = models.CharField(max_length=100)

    def __str__(self):
        return str(self.order_week) + " - " + str(self.order_date) + " - " + str(self.supplier) + " - " + str(self.prod_code_sumitomo) + " - " + str(self.order_qty) + " - " + str(self.fulfill_qty) + " - " + str(self.production_date) + " - " + str(self.trailer_num) + " - " + str(self.port_of_loading) + " - " + str(self.port_of_unlading)
