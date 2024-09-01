from ast import Attribute, FormattedValue
from random import choices
import arabic_reshaper as _
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Customer, Pro_Paper_Type, Product, Order,Design_And_Printing_Specifications,Paper_Specification, Product_Dicription
from .models import Aftar_Print_Services,Gluing_And_Binding_Data,Crushing_Data,Finished_product_and_packing_data

class NewCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Customer_Name', 'Contact_Name','representative', 'Contact_Phone', 'Contact_Email'] 


class NewCustomerALLForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Customer_Sector','Customer_Name', 'representative','Contact_Name', 'Contact_Phone', 'Contact_Email']
         
         
class NewProductForm(forms.ModelForm):
    Product_Name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={ 'class':'form-control'}),label='*إسم المنتج')
    customer_representative = forms.ChoiceField (choices=[('د/عمروالباز','د/عمروالباز'),('ا/عمرو احمد','ا/عمرو احمد'),('م/كريم عبد الغنى','م/كريم عبد الغنى'),('أخرى','أخرى')],widget=forms.Select (attrs={'class':'form-control     '}) ,label=('*ممثل  العميل'))
    Product_Code=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),label='كود العميل ',required=False)
    product_dicription=forms.ModelChoiceField(queryset=Product_Dicription.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),label='وصف المنتج',required=False)
    Product_length=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='*الطول')
    Product_width=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='*العرض') 
    Product_height=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='الإرتفاع',required=False)
    product_avrage_prdect_ammount=forms.CharField(max_length=19,widget=forms.TextInput(attrs={'class':'form-control'}),label='متوسط الكميه المتوقعة',required=False)
    
    class Meta:
        model = Product
        fields = ['Product_Name','customer_representative', 'Product_Code' , 'product_dicription','Product_length', 'Product_width','Product_height' ,'product_avrage_prdect_ammount' ,'Product_Allowable_increase'] 
       

        


class Design_And_Printing_SpecificationsForm(forms.ModelForm):
    pro_design_source=forms.ChoiceField(choices=[('المطبعة','المطبعة'),('العميل','العميل')],widget=forms.Select (attrs={'class':'form-control     '}) ,label='مصدر التصميم' ,required=False)
    pro_design_type=forms.ChoiceField(choices=[('جديد','جديد'),('تعديل','تعديل'),('قديم','قديم')],widget=forms.Select (attrs={'class':'form-control    '}),label='نوع التصميم', required=False)
    attachments_file=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control  '}),label='إرفاق ملف معتمد ',required=False)
    pro_design_ditals=forms.CharField(max_length=999,widget=forms.TextInput(attrs={'class':'form-control '}),label='تفاصيل التصميم ',required=False)
    number_of_sides=forms.ChoiceField(choices=[('وجه','وجه'),('وجهين','وجهين'),('قلاب','قلاب')],widget=forms.Select (attrs={'class':'form-control    '})  ,label='عدد الأوجه',required=False)
    tinted_colors1=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control '}),label='الألوان المخصوصة',required=False)
    tinted_colors2=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control '}),label='',required=False)
    tinted_colors3=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control '}),label='',required=False)
    tinted_colors4=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control '}),label='',required=False)
    tinted_colors5=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control '}),label='',required=False)
    tinted_colors6=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control '}),label='',required=False)
    approved_montage_size = forms.CharField(max_length=50,
                                            widget=forms.TextInput(attrs={'class': 'form-control'}),
                                            label='مقاس المونتاج المعتمد', required=False)
    approved_montage_count = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                                 label='العدد في المونتاج المعتمد', required=False)

    
    class Meta:
        model = Design_And_Printing_Specifications
        fields = '__all__'  


class Paper_SpecificationForm(forms.ModelForm):
    pro_paper_type=forms.ModelChoiceField(queryset=Pro_Paper_Type.objects.all(),widget=forms.Select(attrs={'class':'form-control    '}),label='نوع الورق',required=False)
    pro_paper_gram=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control   '}),label=' الجرامات للورق ',required=False)
    fiber_direction=forms.ChoiceField(choices=(('ضرورية','ضرورية'),('غير ضرورىة','غير ضرورىة')),widget=forms.Select (attrs={'class':'form-control    '}) ,label='إتجاه الألياف',required=False)
    class Meta:
        model = Paper_Specification
        fields = '__all__'
       

       
class Aftar_Print_ServicesForm(forms.ModelForm):
    pro_aftar_print_services_detals=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control '}),label='تفاصيل الخدمة',required=False)

    class Meta:
        model = Aftar_Print_Services
        fields = '__all__'
       


class Crushing_DataForm(forms.ModelForm):
    pro_crushing_data_detals=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control    '}),label='تفاصيل الخدمة' ,required=False)
    class Meta:
        model = Crushing_Data
        fields = '__all__'
        

class Gluing_And_Binding_DataForm(forms.ModelForm):
    pro_Gluing_And_Binding_Data_detals=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control    '}),label='تفاصيل الخدمة ' ,required=False)
    class Meta:
        model = Gluing_And_Binding_Data
        fields = '__all__'
       
             
class Finished_product_and_packing_dataForm(forms.ModelForm):
    pro_finished_product_and_packing_data_type=forms.ChoiceField(choices=([('باندات ورق','باندات ورق'),('استيك','استيك')]),widget=forms.Select (attrs={'class':'form-control   '}) ,label='المنتج النهائي' ,required=False)
    pro_Finished_product_and_packing_data_Baku=forms.ChoiceField(choices=([('ورق','ورق'),('اكياس','اكياس'),('شرنك','شرنك')]),widget=forms.Select (attrs={'class':'form-control   '}) ,label='الباكو',required=False)
    pro_finished_product_and_packing_data_detals=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control   '}),label='تفاصيل الخدمة',required=False)
    class Meta:
        model = Finished_product_and_packing_data
        fields = '__all__'
        
from django import forms
from .models import CorrectiveActions

from django import forms
from .models import CorrectiveActions

class CorrectiveActionsForm(forms.ModelForm):    # اجراءات تصصيصيه المنتجات
    ACTIONS_CHOICES = (
        ('قيد التنفيذ', 'قيد التنفيذ'),
        ('تم التنفيذ', 'تم التنفيذ'),
        ('مرفوض', 'مرفوض'),
        ('تحت الاعتماد', 'تحت الاعتماد'),
    )

    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}), label="التاريخ", required=False)
    complaint_details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label="تفاصيل الشكوى", required=False)
    proposed_solution = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label="الحل المقترح", required=False)
    action_status = forms.ChoiceField(choices=ACTIONS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), label="حالة الإجراء", required=False)
    solution = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label="الحل", required=False)

    class Meta:
        model = CorrectiveActions
        fields = ['date', 'complaint_details', 'proposed_solution', 'action_status', 'solution']
        

        
class NewOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['Order_Details'] 