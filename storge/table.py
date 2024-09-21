from audioop import reverse
import django_tables2 as tables
from .models import *
import django_filters
from django.utils.safestring import mark_safe


class In_StockTable(tables.Table):
    class Meta:
        model = In_stock
        fields = ('date','name','weaight')
        attrs = {"class": "table table-striped table-hover"}


class Out_StockTable(tables.Table):
    class Meta:
        model = Out_Stock
        fields = ('date','in_stock.name','weaight')
        attrs = {"class": "table table-striped table-hover"}

class SupplierTable(tables.Table):
    edit = tables.TemplateColumn(orderable=False,template_code='<a href="{% url "supplier_update" record.pk %}"><i class="fas fa-edit"></i></a></a>', verbose_name='تعديل')
    #name add link to update
    name = tables.TemplateColumn(orderable=False,template_code='<a href="{% url "in_stock_supplier" record.pk %}">{{record.name}}</a>', verbose_name='الاسم')
    class Meta:
        model = Supplier
        template_name = "django_tables2/bootstrap4.html"
        fields = ('name', 'phone', 'address', 'email', 'edit')
        exclude = ('id',)
class InStockNumberTable(tables.Table):
    #edit = tables.TemplateColumn(orderable=False,template_code='<a href="{% url "InStockNumber_update" record.pk %}"><i class="fas fa-edit"></i></a></a>', verbose_name='تعديل')
    number=tables.TemplateColumn(template_code='<a href="{% url "in_stock" record.pk %}">{{record.number}}</a>', verbose_name='العدد')
    class Meta:
        model= InStockNumber
        template_name = "django_tables2/bootstrap4.html"
        fields = ('date','supplier', 'number','status')
        exclude = ('id',)

class IteamTable(tables.Table):
    edit = tables.TemplateColumn(orderable=False,template_code='<a href=""><i class="fas fa-edit"></i></a></a>', verbose_name='تعديل')    
    class Meta:
        model = Iteam
        template_name = "django_tables2/bootstrap4.html"
        fields = ('name','code')
        exclude = ('id','edit')      

class In_stockTable(tables.Table):
    class Meta:
        model = In_stock
        template_name = "django_tables2/bootstrap4.html"
        fields = ('in_stocknumber','date','name','code','weaight','sheet','price')
        exclude = ('id',)

class stocksTable(tables.Table):
    class Meta:
        model = In_stock
        template_name = "django_tables2/bootstrap4.html"
        fields = ('name','code','price','total_weight','total_sheet','in_stocknumber')
        exclude = ('id',) 

class customerTable(tables.Table):
    edit = tables.TemplateColumn(orderable=False,template_code='<a href="{% url "custmer_update" record.pk %}"><i class="fas fa-edit"></i></a></a>', verbose_name='تعديل')  

    name = tables.TemplateColumn(orderable=False,template_code='<a href="{% url "out_stock_customer" record.pk %}">{{record.name}}</a>', verbose_name='الاسم')  
    class Meta:
        model = Customer
        template_name = "django_tables2/bootstrap4.html"
        fields = ('name','phone','address','email','edit')
        exclude = ('id',)

class Out_StockNumberTable(tables.Table):
    #edit = tables.TemplateColumn(orderable=False,template_code='<a href="{% url "OutStockNumber_update" record.pk %}"><i class="fas fa-edit"></i></a></a>', verbose_name='تعديل')  
    number=tables.TemplateColumn(template_code='<a href="{% url "out_stock" record.pk %}">{{record.number}}</a>', verbose_name='العدد')  
    class Meta:
        model= Out_StockNumber
        template_name = "django_tables2/bootstrap4.html"
        fields = ('date','customer', 'number','status')
        exclude = ('id',)


class out_stockTable(tables.Table):

    class Meta:
        model = Out_Stock
        template_name = "django_tables2/bootstrap4.html"
        fields = ('out_stocknumber','date','in_stock.name','in_stock.code','weaight','sheet','price')
        exclude = ('id',)
   



import django_tables2 as tables
from django.db import models
from .models import Iteam, In_stock, Out_Stock

class StockTable(tables.Table):
    edit = tables.TemplateColumn(
        orderable=False,
        template_code='<a href=""><i class="fas fa-edit"></i></a></a>',
        verbose_name='تعديل'
    )
    total_weight = tables.Column(verbose_name='الوزن الإجمالي', empty_values=(), orderable=False)
    total_sheets = tables.Column(verbose_name='عدد الأوراق الإجمالي', empty_values=(), orderable=False)
    
    class Meta:
        model = Iteam
        template_name = "django_tables2/bootstrap4.html"
        fields = ('name', 'code', 'total_weight', 'total_sheets')
        exclude = ('id', 'edit')
        
    def render_total_weight(self, record):
        in_stock_weight = In_stock.objects.filter(iteam=record).aggregate(total_weight=models.Sum('weaight'))['total_weight'] or 0
        out_stock_weight = Out_Stock.objects.filter(iteam=record).aggregate(total_weight=models.Sum('weaight'))['total_weight'] or 0
        total_weight = in_stock_weight - out_stock_weight
        return f"{total_weight:.2f}"
        
    def render_total_sheets(self, record):
        in_stock_sheets = In_stock.objects.filter(iteam=record).aggregate(total_sheets=models.Sum('sheet'))['total_sheets'] or 0
        out_stock_sheets = Out_Stock.objects.filter(iteam=record).aggregate(total_sheets=models.Sum('sheet'))['total_sheets'] or 0
        total_sheets = in_stock_sheets - out_stock_sheets
        return f"{total_sheets:d}"


        