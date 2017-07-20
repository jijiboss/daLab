from import_export import resources
from import_export.widgets import ForeignKeyWidget #widget help convert import value ino corresponding Python object (e.g, INT and DATE)
from import_export import fields #need for fields.FIELD
from .models import Orders, Products, Suppliers


class OrdersResource(resources.ModelResource):

    supplier = fields.Field(
        column_name = 'supplier',
        attribute = 'supplier',
        widget = ForeignKeyWidget(Suppliers, 'supplier')
        )

    prod_code_sumitomo = fields.Field(
        column_name = 'prod_code_sumitomo',
        attribute = 'prod_code_sumitomo',
        widget = ForeignKeyWidget(Products, 'prod_code_sumitomo')
        )

    class Meta:
        model = Orders

        #This returns "pork01.models.DoesNotExist: Suppliers matching query does not exist."
#        import_id_fields = ['order_week', 'order_date', 'supplier', 'prod_code_sumitomo', 'order_qty', 'fulfill_qty', 'production_date', 'trailer_num', 'port_of_loading', 'port_of_unlading']

        #This returns "KeyError: 'id' error
#        fields = ['order_week', 'order_date', 'supplier', 'prod_code_sumitomo', 'order_qty', 'fulfill_qty', 'production_date', 'trailer_num', 'port_of_loading', 'port_of_unlading']

        import_id_fields = ('prod_code_sumitomo', )
        fields = ('order_week', 'order_date', 'supplier', 'prod_code_sumitomo', 'order_qty', 'fulfill_qty', 'production_date', 'trailer_num', 'port_of_loading', 'port_of_unlading',)
        import_order = ('order_week', 'order_date', 'id', 'supplier', 'prod_code_sumitomo', 'order_qty', 'fulfill_qty', 'production_date', 'trailer_num', 'port_of_loading', 'port_of_unlading',)
