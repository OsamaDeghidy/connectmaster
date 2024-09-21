from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Supplier)
admin.site.register(Main_categorey)
admin.site.register(Sub_categorey)
admin.site.register(Peper_type_country)
admin.site.register(Degree)
admin.site.register(Gram_Categore)
admin.site.register(linght)
admin.site.register(width)
#iteam
admin.site.register(Iteam)
admin.site.register(In_stock)

#اصناف 
admin.site.register(In_stoke_detals)
admin.site.register(Customer)
admin.site.register(InStockNumber)
admin.site.register(Out_Stock)
admin.site.register(Out_StockNumber)


