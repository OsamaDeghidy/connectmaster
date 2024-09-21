#impotmodels
import datetime
from django import forms
from .models import *
from django.forms import formset_factory

class SupplierForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Supplier
        fields = ('name', 'phone', 'email', 'address')


class InStockNumberForm(forms.ModelForm):
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = InStockNumber
        fields = ('supplier',)
        exclude = ('date','number','status')


class InStockNumberForm2(forms.ModelForm):
    
    status = forms.ChoiceField(choices=InStockNumber.STATUS, widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    class Meta:
        model = InStockNumber
        fields = ('status',)
        exclude = ('date','number','supplier')


class IteamForm(forms.ModelForm):    
    main_categorey = forms.ModelChoiceField(queryset=Main_categorey.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    sub_categorey = forms.ModelChoiceField(queryset=Sub_categorey.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    degree = forms.ModelChoiceField(queryset=Degree.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    peper_type_country = forms.ModelChoiceField(queryset=Peper_type_country.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    gram_categore = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_value=999)
    linght = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_value=9999)
    width = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_value=9999)
    class Meta:
        model = Iteam
        fields = ( 'main_categorey', 'sub_categorey', 'degree', 'peper_type_country', 'gram_categore', 'linght', 'width',)  
        exclude = ('name ','code','id',)      


class In_stockForm(forms.ModelForm):
    weaight = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control col-lg-10','placeholder': 'kg'}),label='الوزن',required=False)
    sheet = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control col-lg-10','placeholder': 'sheets'}),label='العدد ',required=False,)
    price = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control col-lg-10','placeholder': 'LE'}),label='السعر',required=False)
    iteam = forms.ModelChoiceField(queryset=Iteam.objects.all(), widget=forms.Select(attrs={'class': 'form-control col-lg-12'}),label=' اسم الصنف ',required=False)  
    class Meta:
        model = In_stock
        fields = ('iteam', 'weaight', 'sheet', 'price')
        exclude = ('id','name','code','supplier','date')

In_stockFormSet = formset_factory(In_stockForm, extra=10)


class CustomerForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Customer
        fields = ('name', 'phone', 'email', 'address')      
        exclude = ('id',)



class Out_StockNumberForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Out_StockNumber
        fields = ('customer',)
        exclude = ('date','number','status')


class Out_StockNumberForm2(forms.ModelForm):
    status = forms.ChoiceField(choices=Out_StockNumber.STATUS, widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    class Meta:
        model = Out_StockNumber
        fields = ('status',)
        exclude = ('date','number','customer')





class Out_stokeForm (forms.ModelForm):
    weaight = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control col-lg-10','placeholder': 'kg'}),label='الوزن',required=False)
    sheet = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control col-lg-10','placeholder': 'sheets'}),label='العدد ',required=False,)
    price = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control col-lg-10','placeholder': 'LE'}),label='السعر',required=False)
    in_stock= forms.ModelChoiceField(queryset=In_stock.objects.all(), widget=forms.Select(attrs={'class': 'form-control col-lg-12'}),label=' اسم الصنف ',required=False)
    in_stock_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Out_Stock
        fields = ('in_stock', 'weaight', 'sheet', 'price','in_stock_id')
        exclude = ('id','name','code','date','out_stocknumber')

        
      

Out_stokeFormSet = formset_factory(Out_stokeForm, extra=3)

class Out_stoke_allForm (forms.ModelForm):
    weaight = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control col-lg-10','placeholder': 'kg'}),label='الوزن',required=False)
    sheet = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control col-lg-10','placeholder': 'sheets'}),label='العدد ',required=False)
    price = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control col-lg-10','placeholder': 'LE'}),label='السعر',required=False)
    in_stock= forms.ModelChoiceField(queryset=In_stock.objects.all(), widget=forms.Select(attrs={'class': 'form-control col-lg-12'}),label=' اسم الصنف ',required=False)
    class Meta:
        model = Out_Stock
        fields = ('in_stock', 'weaight', 'sheet', 'price')
        exclude = ('id','name','code','customer','date','out_stocknumber')




             