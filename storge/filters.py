import django_filters
from django import forms

from storge.forms import In_stockForm
from .models import *
from django_filters import DateFilter, CharFilter



class In_StockFilter(django_filters.FilterSet):
    iteam = django_filters.ModelChoiceFilter(queryset=Iteam.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}),label=' اسم الصنف ',required=False)
    code  = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الرقم')
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}),label='التاريخ')

    class Meta:
        model = In_stock
        fields = '__all__'
        exclude = ['id', 'supplier', 'date', 'name', 'price','sheet','weaight','in_stocknumber','supplier']

class Out_StockFilter(django_filters.FilterSet):
    in_stock=django_filters.ModelChoiceFilter(queryset=In_stock.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}),label=' اسم الصنف ',required=False)
    iteam=django_filters.ModelChoiceFilter(queryset=Iteam.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}),label=' اسم الصنف ',required=False)
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}),label='التاريخ')
    class Meta:
        model = Out_Stock
        fields = '__all__'
        exclude = ['id','date','weaight','sheet','price','out_stocknumber','in_stock','iteam','customer']

class SupplierFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الاسم ')
    phone = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الهاتف')
    email = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الايميل')

    class Meta:
        model = Supplier
        fields = '__all__'
        exclude = ['id', 'user', 'name', 'phone', 'address', 'email']        

class InStockNumberFilter(django_filters.FilterSet):
    number = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الرقم')
    supplier = django_filters.ModelChoiceFilter(queryset=Supplier.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}),label='المورد')
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}),label='التاريخ')
    class Meta:
        model = InStockNumber
        fields = '__all__'
        exclude = ['id', 'user', 'supplier', 'date', 'number','status']


class IteamFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الاسم ')
    code = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الكود')
    #main_categorey = django_filters.ModelChoiceFilter(queryset=Main_categorey.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}),label='القسم الرئيسي')
    sub_categorey = django_filters.ModelChoiceFilter(queryset=Sub_categorey.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}),label='القسم الفرعي')
    #peper_type_country = django_filters.ModelChoiceFilter(queryset=Peper_type_country.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}),label='الدولة المصدرة')
    #degree = django_filters.ModelChoiceFilter(queryset=Degree.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}),label='الدرجة')
    #linght = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الطول')
    #width = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='العرض')


    class Meta:
        model = Iteam
        fields = '__all__'
        exclude = ['id', 'user', 'name', 'code', 'main_categorey', 'sub_categorey', 'peper_type_country', 'degree', 'gram_categore','description','width','linght']


class In_stockFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الاسم')
    code = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الكود')
    iteam = django_filters.ModelChoiceFilter(queryset=Iteam.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}),label='الصنف')
    date = django_filters.DateFilter(field_name='date',widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}),label='التاريخ')
    
    #price = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='السعر')
    #total = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الاجمالي')

    class Meta:
        model = In_stock
        fields = '__all__'
        exclude = ['id', 'code', 'iteam', 'supplier', 'date', 'name', 'price','sheet','weaight','in_stocknumber']

class CustomerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الاسم')
    phone = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الهاتف')
    email = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الايميل')

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['id', 'user', 'name', 'phone', 'address', 'email']

class Out_StockNumberFilter(django_filters.FilterSet):
    number = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الرقم')
    customer = django_filters.ModelChoiceFilter(queryset=Customer.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}),label='العميل')
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}),label='التاريخ')
    class Meta:
        model = Out_StockNumber
        fields = '__all__'
        exclude = ['id', 'user', 'customer', 'date', 'number','status']

class  out_stockFilter (django_filters.FilterSet):  
    in_stock_name = django_filters.CharFilter(field_name='in_stock__name',lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الاسم')
    in_stock_code = django_filters.CharFilter(field_name='in_stock__code',lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control ',}),label='الكود')
   
    date = django_filters.DateFilter(field_name='date',widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}),label='التاريخ')

    class Meta:
        model = Out_Stock
        fields = '__all__'
        exclude = ['id','date','weaight','sheet','price','out_stocknumber','in_stock','iteam']
    
#In_stoke_detalsFilter
