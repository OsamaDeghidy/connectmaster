from django.contrib import admin
from .models import Machine, Machine_Order
from machines import models


# Register your models here.
admin.site.register(Machine)
admin.site.register(Machine_Order)


