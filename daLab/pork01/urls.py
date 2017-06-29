"""
URLs just for the 'pork01' app of the 'proto01' project
	r'^$'

	'r' => it's a regular epression!
	'^' => The beginning
	'$' => The end

"""

from django.conf.urls import url
from . import views

#Define the name space 'pork01'
app_name = 'pork01'

urlpatterns = [
    #url(r'^$', views.index, name='index'),

	#/pork01/
	#invokes the IndexView class and passes it as a view
    url(r'^$', views.IndexView.as_view(), name='index'),

	#/pork01/81030/
	#invokes "DetailView"class in views.py passing numeric <product_code as pk> as the argument (?P<>)
	#the DetailView expects a primarykey so use pk
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='product_detail'),

	#/pork01/products/add
    url(r'products/add/$', views.ProductsCreate.as_view(), name='product-add'),

	#/pork01/products/81030
    url(r'products/(?P<pk>[0-9]+)/$', views.ProductsUpdate.as_view(), name='product-update'),

	#/pork01/products/81030/delete
    url(r'products/(?P<pk>[0-9]+)/delete/$', views.ProductsDelete.as_view(), name='product-delete'),
]
