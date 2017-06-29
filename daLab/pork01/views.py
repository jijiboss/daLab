from django.views import generic
from django.views.generic.edit import CreateView #form to create a new object
from django.views.generic.edit import UpdateView #form to nodify a new object
from django.views.generic.edit import DeleteView #form to delete a new object
from django.core.urlresolvers import reverse_lazy
from .models import Suppliers, Products


#from django.shortcuts import render
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("<H1>Pork web site prototype 01</H1>")

#() after class names means "inherit from"

#replaces the index method
class IndexView(generic.ListView):
	template_name='pork01/index.html'
	context_object_name='object_list' #ListView returns "object_list" by default but cn be overridden with using this variable

	def get_queryset(self):
		return Products.objects.all() #this returns an object called "object_list"s


#replaces the product_detail method
class DetailView(generic.DetailView):
	model = Products
	template_name ='pork01/detail.html'


#Form to allow users to create a new product model entry
class ProductsCreate(CreateView):
	model = Products
	#The attributes to allow users to populate
	fields = ['supplier', 'prod_code_supplier', 'item_supplier', 'prod_code_sumitomo', 'item_sumitomo', 'is_favorite']

#Form to allow users to update a new product model entry
class ProductsUpdate(UpdateView):
	model = Products
	#The attributes to allow users to populate
	fields = ['supplier', 'prod_code_supplier', 'item_supplier', 'prod_code_sumitomo', 'item_sumitomo', 'is_favorite']

class ProductsDelete(DeleteView):
	model = Products
	success_url = reverse_lazy('pork01:index')
