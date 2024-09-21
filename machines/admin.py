from django.contrib import admin
from .models import Machine, Machine_Order
from machines import models
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin
class MachineAdmin(ImportExportModelAdmin):
    pass

class MachineOrderAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Machine, MachineAdmin)
admin.site.register(Machine_Order, MachineOrderAdmin)




