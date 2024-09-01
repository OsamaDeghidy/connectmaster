from django.contrib import admin
from .models import Sector, Customer, Product, CorrectiveActions
from .models import Product_Dicription,Finished_product_and_packing_data,Gluing_And_Binding_Data,Crushing_Data,Aftar_Print_Services,Paper_Specification,Design_And_Printing_Specifications,Pro_Paper_Type
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from django.contrib import admin
from .models import Representative

class RepresentativeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Representative, RepresentativeAdmin)

class Customerdp(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Customer_Name', 'customer_code')
    list_filter = ('Customer_Sector',)
    search_fields = ('Customer_Name', 'customer_code',) 
    ordering = ('Customer_Name', 'customer_code')
    pass
class Sectordp(ImportExportModelAdmin):
    pass
class Productdp(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Product_Name', 'Product_MyCode')
    list_filter = ('Product_Sector','Product_Customer',)
    search_fields = ('Product_Name', 'Product_MyCode') 
    ordering = ('Product_Name', 'Product_MyCode')
    pass
class Design_And_Printing_Specificationsdp(ImportExportModelAdmin):
    pass
class Pro_Paper_Typedp(ImportExportModelAdmin):
    pass
class Paper_Specificationdp(ImportExportModelAdmin):
    pass
class Aftar_Print_Servicesdp(ImportExportModelAdmin):
    pass
class Crushing_Datadp(ImportExportModelAdmin):
    pass
class Gluing_And_Binding_Datadp(ImportExportModelAdmin):
    pass
class Finished_product_and_packing_datadp(ImportExportModelAdmin):
    pass

class CorrectiveActionsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('date', 'complaint_details', 'proposed_solution', 'action_status', 'solution')
    list_filter = ('action_status', 'date')
    search_fields = ('complaint_details', 'proposed_solution', 'solution')

admin.site.register(CorrectiveActions, CorrectiveActionsAdmin)





admin.site.register(Sector,Sectordp)
admin.site.register(Customer,Customerdp)

admin.site.register(Product,Productdp)
admin.site.register(Design_And_Printing_Specifications,Design_And_Printing_Specificationsdp)
admin.site.register(Pro_Paper_Type,Pro_Paper_Typedp)
admin.site.register(Paper_Specification,Paper_Specificationdp)
admin.site.register(Aftar_Print_Services,Aftar_Print_Servicesdp)
admin.site.register(Crushing_Data,Crushing_Datadp)
admin.site.register(Gluing_And_Binding_Data,Gluing_And_Binding_Datadp)
admin.site.register(Finished_product_and_packing_data,Finished_product_and_packing_datadp)

class ProductDicriptionAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Product_Dicription, ProductDicriptionAdmin)