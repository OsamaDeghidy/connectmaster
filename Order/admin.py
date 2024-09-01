from typing import Sequence
from django.contrib import admin
#import simple_history admin to show history of the model
from .models import Order, OrderDeliveryDate, Paper_and_cardboard_data, Order_states
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin


class OrderDeliveryDateAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    
    list_display = ['RDD', 'EDD']

admin.site.register(OrderDeliveryDate, OrderDeliveryDateAdmin)




class PaperAndCardboardDataAdmin(ImportExportModelAdmin):
    pass

class OrderStatesAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Paper_and_cardboard_data, PaperAndCardboardDataAdmin)
admin.site.register(Order_states, OrderStatesAdmin)


class OrderAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('Ord_work_order_number', 'Ord_states', 'get_product_name', 'Ord_Customer_Name')
    list_filter = ('Ord_states',)
    search_fields = ('Ord_work_order_number',)
    ordering = ('Ord_work_order_number',)
    list_editable = ('Ord_states',)

    def get_product_name(self, obj):
        return obj.Ord_Product.Product_Name
    get_product_name.short_description = 'Product Name'

# Register your models here.
admin.site.register(Order, OrderAdmin)

