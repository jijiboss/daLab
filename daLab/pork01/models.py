from django.db import models
from django.core.urlresolvers import reverse
from django.contrib import admin #for the Admin view

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

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('supplier','prod_code_supplier', 'item_supplier', 'prod_code_sumitomo', 'item_sumitomo')


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


class OrdersAdmin(admin.ModelAdmin):
    #http://blog.endpoint.com/2012/02/dowloading-csv-file-with-from-django.html

    #for the tabular view
    list_display = ('order_week', 'order_date', 'supplier', 'prod_code_sumitomo',
     'order_qty', 'fulfill_qty', 'production_date', 'trailer_num', 'port_of_loading', 'port_of_unlading')

     #For the "download in CSV format" option
    actions = ['download_csv']

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        import io #Implements the same interface as file but only in memory and not disk
        #Open a file stream in write to a writer object.

        #This approach will write the file to the disk.
        #f = open('some.csv', 'wb') #This would open the file in Binary format so if i try to write str then throws an error
        #f = open('some.csv', 'w')
        #writer = csv.writer(f)

        #This approach will write to memory and not to disk.
        f = io.StringIO()
        writer = csv.writer(f)

        #Wite the column headers
        writer.writerow(["order_week", "order_date", "supplier", "prod_code_sumitomo", "order_qty", "fulfill_qty", "production_date", "trailer_num", "port_of_loading", "port_of_unlading"])
        #Write the query results
        for s in queryset:
            writer.writerow([s.order_week, s.order_date, s.supplier, s.prod_code_sumitomo, s.order_qty, s.fulfill_qty, s.production_date, s.trailer_num, s.port_of_loading, s.port_of_unlading])

#        f.close() #This is needed only if using the write-to-disk method (not StringIO)
        #This prompts the user to open the new CSV file
#        f = open('some.csv', 'r') #This is needed only if using the write-to-disk method (not StringIO)
        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=order-report.csv'
        return response

    #This adds an entry in the Action drop down on the admin page
    download_csv.short_description = "Download CSV for selected rows."
