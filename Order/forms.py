from ast import Attribute, FormattedValue
from cProfile import label
from email.policy import default
from random import choices
import arabic_reshaper as _
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Order, Order_states, OrderDeliveryDate, Paper_and_cardboard_data,Order_states

class OrderDeliveryDateForm(forms.ModelForm):
    RDD = forms.DateField(label='RDD', widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}),required=False)
    EDD = forms.DateField(label='EDD', widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}),required=False)


    class Meta:
        model = OrderDeliveryDate
        fields = ['RDD', 'EDD']
        


class RDDForm(forms.ModelForm):
    RDD = forms.DateField(label='RDD', widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}),required=False)

    class Meta:

        model = OrderDeliveryDate
        fields = ['RDD']

class EDDForm(forms.ModelForm):
    EDD = forms.DateField(label='EDD', widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}),required=False)

    class Meta:
        model = OrderDeliveryDate
        fields = ['EDD']
        

class NewOrderForm(forms.ModelForm):
    #Ord_Created_Dt = forms.DateField(label='التاريخ', widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}),required=False)
    #Ord_work_order_number = forms.CharField(label='رقم امر الشغل', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    #customer_representative = forms.CharField(label='ممثل العميل', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    #Customer_product_code = models.CharField(max_length=50, null=True, blank=True,verbose_name='كود المنتج للعميل')
    #Company_product_code = models.CharField(max_length=50, null=True, blank=True,verbose_name='كود المنتج للشركة')
    Ord_Required_quantity = forms.CharField(label='الكمية المطلوبة', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_import_order_number = forms.CharField(label='رقم امر التوريد', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
#بيانات التصميم والتجهيزات الفنيه 
    Ord_Operation_type =forms.ChoiceField(choices=[('',''),('مكررة','مكررة'),('جديدة','جديدة'),('تعديل','تعديل')],label='نوع العملية',widget=forms.Select(attrs={'class':'form-control'}),required=False)
    Ord_Operation_modification_type =forms.CharField(label='نوع التعديل', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
#Dimensions الابعاد
    #Ord_Length = forms.CharField(label='الطول', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    #Ord_Width = forms.CharField(label='العرض', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    #Ord_Height = forms.CharField(label='الارتفاع', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
#-----------------------------------------------------------------------------------------------------------------------
    Ord_states =forms.ModelChoiceField(queryset=Order_states.objects.all(),label='الحالة',widget=forms.Select(attrs={'class':'form-control'}),required=False)
    Ord_montage_size = forms.CharField(label='مقاس المونتاج', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_zincs = forms.CharField(label='الزنكات', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Number_the_montage =  forms.CharField(label='عدد فى المونتاج', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_form = forms.CharField(label='فورم', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Annexes_design_data = forms.CharField(label='بيانات التصميم والتجهيزات الفنيه', max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Other_supplies = forms.CharField(label='لوازم اخرى', max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
#-----------------بيانات الطباعة------------------------------------------------------------------------------------------------------
    Ord_type_print= forms.ChoiceField(choices=[('',''),('ربع','ربع'),('نص','نص'),('فرخ','فرخ')],label='الطباعة ',widget=forms.Select(attrs={'class':'form-control'}),required=False)
    Ord_colors_nember = forms.CharField(label='عدد الالوان', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_number_of_faces = forms.CharField(label='عدد الاوجه', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_the_machine = forms.CharField(label='الماكينة', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_colors_are_picture = forms.CharField(label='الوان  صورة', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_custom_colors = forms.CharField(label='الوان المخصوصة', max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_print_note = forms.CharField(label='ملاحظات الطباعة', max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
#----------------- خدمات ما بعد الطباعه------------------------------------------------------------------------------------------------------
    Ord_cellophane_type = forms.CharField(label='نوع السيلوفان', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_face_number = forms.CharField(label='عدد الاوجه', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Maiden_size = forms.CharField(label='مقاس البكر', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Other_services = forms.ChoiceField(choices=[('',''),('ورنيش مائى','ورنيش مائى'),('يوفى','يوفى'),('ورنيش دهنى','ورنيش دهنى'),('يوفى ثم ورنيش','يوفى ثم ورنيش'),('سبوت','سبوت'),('اخرى','اخرى')],label='خدمات اخرى',widget=forms.Select(attrs={'class':'form-control'}),required=False)
    Ord_Description_services = forms.CharField(label='وصف الخدمة', max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Notes = forms.CharField(label='ملاحظات', max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
#-----------------خدمات التكسير ------------------------------------------------------------------------------------------------------
    Ord_Breaking_services = forms.ChoiceField(choices=[('',''),('فورمه جديد','فورمه جديد'),('فورمه قديمه','فورمه قديمه')],label='خدمات التكسير',widget=forms.Select(attrs={'class':'form-control'}),required=False)
    Ord_Breaking_services_two= forms.ChoiceField(choices=[('',''),('شباك جديد','شباك جديد'),('شباك قديم','شباك قديم')],label='خدمات التكسير',widget=forms.Select(attrs={'class':'form-control'}),required=False)
    Ord_Chop_code = forms.CharField(label='كود/عدد الفورمه', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_form_of = forms.CharField(label='فورمه من', max_length=450, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Machine = forms.CharField(label='الماكينة', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Number_Reg = forms.CharField(label='عدد الريج', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Attachments = forms.CharField(label='المرفقات', max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Note_Breaking = forms.CharField(label='ملاحظات التكسير', max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Others = forms.ChoiceField(choices=[('',''),('كفراج','كفراج'),('تنظيف','تنظيف'),('اخرى','اخرى')] ,label='اخرى',widget=forms.Select(attrs={'class':'form-control'}),required=False)
#-----------------خدمات اللصق والتجليد ------------------------------------------------------------------------------------------------------
    Ord_Gluing =  forms.ChoiceField(choices=[('',''),('آلى','آلى'),('يدوى','يدوى'),('تجليد','تجليد')],label='تلزيق',widget=forms.Select(attrs={'class':'form-control'}),required=False)
    Ord_Note_Gluing = forms.CharField(label='ملاحظات التلزيق', max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_number_corners = forms.CharField(label='عدد الاركان', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Gluing_Description = forms.CharField(label='وصف التلزيق', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_machine_name = forms.CharField(label='اسم الماكينة', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Complete_Product =  forms.ChoiceField(choices=[('',''),('باندات','باندات'),('استيك','استيك'),('يدوى','يدوى'),('اخرى','اخرى')],label='المنتج التام',widget=forms.Select(attrs={'class':'form-control'}),required=False)
    Ord_number_pandas = forms.CharField(label='عدد/الباندات', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Packing =  forms.ChoiceField(choices=[('',''),('صناديق','صناديق'),('كرافت/ورق لف','كرافت/ورق لف'),('اكياس','اكياس')],label='التغليف',widget=forms.Select(attrs={'class':'form-control'}),required=False)
    Ord_number_pacu = forms.CharField(label='العدد/الباكو', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Required_materials = forms.CharField(label='المواد المطلوبة', max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Ord_Delivery_Instructions = forms.CharField(label='تعليمات التسليم', max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)

    class Meta:
        model = Order
        fields =('__all__')
        exclude = ['Order_Details','Ord_Cust_Name','Ord_Product','Ord_Created_By','Ord_work_order_number']
          

class New_Paper_and_cardboard_data_Form (forms.ModelForm):
    CARD_Work_order_number_in_chart= forms.CharField(label='رقم امر الشغل فى  الشيتر', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    
    CARD_note_Paper_type_and_size = forms.CharField(label='ملاحظات على نوع الورق ومقاسة', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Cut_size = forms.CharField(label='مقاس قص السكينه', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_fiber_direction = forms.CharField(label='اتجاه الالياف', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Total_cut_and_fiber = forms.CharField(label=' الاجمالى للقطع والالياف', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Total_weight = forms.CharField(label='العدد الاجمالى', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
#-----------------main data------------------------------------------------------------------------------------------------------
    CARD_Supplier = forms.CharField(label='المورد', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Paper_type_and_size = forms.CharField(label='نوع الورق ومقاسة', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Grame = forms.CharField(label='الجرامة', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_long_number = forms.CharField(label='العدد الطوايل', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Gross_weight = forms.CharField(label='الوزن القائم', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Net_weight = forms.CharField(label='الوزن الصافى', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Number = forms.CharField(label='العدد', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
#----------------- data 1-------------------------------------------------------------------------------------------------------------------------
    CARD_Supplier_1 = forms.CharField(label='المورد', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Paper_type_and_size_1 = forms.CharField(label='نوع الورق ومقاسة', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Grame_1 = forms.CharField(label='الجرامة', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_long_number_1 = forms.CharField(label='العدد الطوايل', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Gross_weight_1 = forms.CharField(label='الوزن القائم', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Net_weight_1 = forms.CharField(label='الوزن الصافى', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Number_1 = forms.CharField(label='العدد', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
#----------------- data 2-------------------------------------------------------------------------------------------------------------------------
    CARD_Supplier_2 = forms.CharField(label='المورد', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Paper_type_and_size_2 = forms.CharField(label='نوع الورق ومقاسة', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Grame_2 = forms.CharField(label='الجرامة', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_long_number_2= forms.CharField(label='العدد الطوايل', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Gross_weight_2 = forms.CharField(label='الوزن القائم', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Net_weight_2 = forms.CharField(label='الوزن الصافى', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Number_2 = forms.CharField(label='العدد', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
#----------------- data 3-------------------------------------------------------------------------------------------------------------------------
    CARD_Supplier_3 = forms.CharField(label='المورد', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Paper_type_and_size_3 = forms.CharField(label='نوع الورق ومقاسة', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Grame_3 = forms.CharField(label='الجرامة', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_long_number_3 = forms.CharField(label='العدد الطوايل', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Gross_weight_3 = forms.CharField(label='الوزن القائم', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Net_weight_3 = forms.CharField(label='الوزن الصافى', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    CARD_Number_3 = forms.CharField(label='العدد', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)

    class Meta:
        model = Paper_and_cardboard_data
        fields = ('__all__')
        exclude = ['CARD_Order']


class Order_states_Form (forms.ModelForm):
    class Meta:
        model = Order_states
        fields = ['name',]
