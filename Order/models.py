from audioop import reverse
from email.policy import default
from turtle import update
from django.db import models
from django.db.models.fields import CharField, DateField, EmailField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.files import ImageField
from itertools import count
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from isort import code
from multiselectfield import MultiSelectField
from simple_history.models import HistoricalRecords




class OrderDeliveryDate(models.Model):
    RDD = models.DateField(null=True, blank=True)
    EDD = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"RDD: {self.RDD}, EDD: {self.EDD}"



# Create your models here.
# Orders Table
class Order(models.Model):
    
    Ord_delivery_date = models.OneToOneField('OrderDeliveryDate', on_delete=models.CASCADE, null=True, blank=True)
#---------------------------------------------------------------------------------------------------
    Ord_code_Edited = models.CharField(max_length=50,editable=False)
    Ord_Created_Dt = models.DateField(auto_now_add=True)
    Ord_Product = models.ForeignKey('Work_Orders.Product', on_delete=models.CASCADE, null=True, blank=True)
    Ord_Customer_Name = models.ForeignKey('Work_Orders.Customer', on_delete=models.CASCADE, null=True, blank=True, verbose_name='اسم العميل')
    Ord_Created_By = models.ForeignKey(User,related_name='Orders',on_delete=models.CASCADE, null=True, blank=True)
    Ord_updated_by = models.ForeignKey(User,related_name='Orders_updated',on_delete=models.CASCADE, null=True, blank=True)
    history = HistoricalRecords()
    #Ord_code_pro = models.CharField(max_length=50,editable=False,unique=True)
    #Ord_code_pro_update = models.CharField(max_length=50,editable=False)
    Order_Details = models.TextField(max_length=40, null=True, blank=True, verbose_name='تفاصيل الطلب',)
    Ord_work_order_number = models.CharField(max_length=50,unique=True,verbose_name='رقم امر الشغل') # كود order
    #Customer_product_code = models.CharField(max_length=50, null=True, blank=True,verbose_name='كود المنتج للعميل')
    #Company_product_code = models.CharField(max_length=50, null=True, blank=True,verbose_name='كود المنتج للشركة')
    Ord_Required_quantity = models.CharField(max_length=50, null=True, blank=True,verbose_name='الكمية المطلوبة')
    Ord_import_order_number = models.CharField(max_length=50, null=True, blank=True,verbose_name='رقم امر التورد')
#بيانات التصميم والتجهيزات الفنيه 
    Ord_Operation_type = MultiSelectField(choices=[('',''),('مكررة','مكررة'),('جديدة','جديدة'),('تعديل','تعديل')],null=True, blank=True,verbose_name='نوع العملية',max_length=50)
    Ord_Operation_modification_type =models.CharField(max_length=100, null=True, blank=True,verbose_name='نوع التعديل')
#Dimensions الابعاد
    #Ord_Length = models.CharField(max_length=50, null=True, blank=True,verbose_name='الطول')
    #Ord_Width = models.CharField(max_length=50, null=True, blank=True,verbose_name='العرض')
    #Ord_Height = models.CharField(max_length=50, null=True, blank=True,verbose_name='الارتفاع')
#-----------------------------------------------------------------------------------------------------------------------
    Ord_montage_size = models.CharField(max_length=50, null=True, blank=True,verbose_name='مقاس المونتاج')
    Ord_zincs = models.CharField(max_length=50, null=True, blank=True,verbose_name='الزنكات')
    Ord_Number_the_montage = models.CharField(max_length=50, null=True, blank=True,verbose_name='عدد فى المونتاج')
    Ord_form = models.CharField(max_length=50, null=True, blank=True,verbose_name='فورمة')
    Ord_Annexes_design_data = models.CharField(max_length=250, null=True, blank=True,verbose_name='المرفقات للتصميم والتجهيزات الفنيه')
    Ord_Other_supplies = models.CharField(max_length=250, null=True, blank=True,verbose_name='لوازم اخرى')
#-----------------بيانات الطباعة------------------------------------------------------------------------------------------------------
    Ord_type_print =MultiSelectField(choices=[('',''),('ربع','ربع'),('نص','نص'),('فرخ','فرخ')],null=True, blank=True,max_length=50,verbose_name=' الطباعة')
    Ord_colors_nember = models.CharField(max_length=10, null=True, blank=True,verbose_name='عدد الالوان')
    Ord_number_of_faces = models.CharField(max_length=50, null=True, blank=True,verbose_name='عدد الاوجه')
    Ord_the_machine = models.CharField(max_length=50, null=True, blank=True,verbose_name='الماكينة')
    Ord_colors_are_picture = models.CharField(max_length=50, null=True, blank=True,verbose_name='الوان  صورة')
    Ord_custom_colors = models.CharField(max_length=500, null=True, blank=True,verbose_name='الوان مخصوصة')
    Ord_print_note = models.CharField(max_length=250, null=True, blank=True,verbose_name='ملاحظات الطباعة')
#----------------- بيانـات الورق و الكرتون الفعلى------------------------------------------------------------------------------------------------------   
    Ord_states =models.ForeignKey('Order_states', on_delete=models.CASCADE, null=True, blank=True, verbose_name='المرحلة')
#----------------- خدمات ما بعد الطباعه------------------------------------------------------------------------------------------------------
    Ord_cellophane_type = models.CharField(max_length=50, null=True, blank=True,verbose_name='نوع السيلوفان')
    Ord_face_number = models.CharField(max_length=50, null=True, blank=True,verbose_name='عدد الوجه')
    Ord_Maiden_size = models.CharField(max_length=50, null=True, blank=True,verbose_name='مقاس البكر')
    Ord_Other_services = MultiSelectField(choices=[('',''),('ورنيش مائى','ورنيش مائى'),('يوفى','يوفى'),('ورنيش دهنى','ورنيش دهنى'),('يوفى ثم ورنيش','يوفى ثم ورنيش'),('سبوت','سبوت'),('اخرى','اخرى')],null=True, blank=True,verbose_name='خدمات اخرى',max_length=100)
    Ord_Description_services = models.CharField(max_length=250, null=True, blank=True,verbose_name='وصف الخدمات')
    Ord_Notes = models.CharField(max_length=250, null=True, blank=True,verbose_name='ملاحظات')
#-----------------خدمات التكسير ------------------------------------------------------------------------------------------------------
    Ord_Breaking_services = MultiSelectField(choices=[('',''),('فورمه جديد','فورمه جديد'),('فورمه قديمه','فورمه قديمه')],null=True, blank=True,verbose_name='خدمات التكسير',max_length=100)
    Ord_Breaking_services_two=MultiSelectField(choices=[('',''),('شباك جديد','شباك جديد'),('شباك قديم','شباك قديم')],null=True, blank=True,verbose_name='خدمات التكسير',max_length=100)
    Ord_Chop_code = models.CharField(max_length=50, null=True, blank=True,verbose_name='كود/عدد الفورمه')
    Ord_form_of = models.CharField(max_length=500, null=True, blank=True,verbose_name='فورمه من')
    Ord_Machine = models.CharField(max_length=50, null=True, blank=True,verbose_name='الماكينة')
    Ord_Number_Reg = models.CharField(max_length=50, null=True, blank=True,verbose_name='عدد الريج')
    Ord_Attachments = models.CharField(max_length=250, null=True, blank=True,verbose_name='المرفقات')
    Ord_Note_Breaking = models.CharField(max_length=250, null=True, blank=True,verbose_name='ملاحظات التكسير')
    Ord_Others = MultiSelectField(choices=[('',''),('كفراج','كفراج'),('تنظيف','تنظيف'),('اخرى','اخرى')],null=True, blank=True,verbose_name='اخرى',max_length=100)
#-----------------خدمات اللصق والتجليد ------------------------------------------------------------------------------------------------------
    Ord_Gluing = MultiSelectField(choices=[('',''),('آلى','آلى'),('يدوى','يدوى'),('تجليد','تجليد')],null=True, blank=True,verbose_name='تلزيق ',max_length=100,)
    Ord_Note_Gluing = models.CharField (max_length=250 ,null=True,blank=True,verbose_name='ملاحظات التلزيق')
    Ord_number_corners = models.CharField (max_length=50 ,null=True,blank=True,verbose_name='عدد الاركان')
    Ord_Gluing_Description = models.CharField (max_length=250 ,null=True,blank=True,verbose_name='الوصف')
    Ord_machine_name = models.CharField (max_length=50 ,null=True,blank=True,verbose_name='اسم الماكينة')
    Ord_Complete_Product = MultiSelectField(choices=[('',''),('باندات','باندات'),('استيك','استيك'),('يدوى','يدوى'),('اخرى','اخرى')],null=True, blank=True,verbose_name='المنتج التام',max_length=100)
    Ord_number_pandas = models.CharField (max_length=50 ,null=True,blank=True,verbose_name='عدد/الباندات')
    Ord_Packing = MultiSelectField(choices=[('',''),('صناديق','صناديق'),('كرافت/ورق لف','كرافت/ورق لف'),('اكياس','اكياس')],null=True, blank=True,verbose_name='التغليف',max_length=100)
    Ord_number_pacu = models.CharField (max_length=15 ,null=True,blank=True,verbose_name='العدد/الباكو')
    Ord_Required_materials = models.CharField (max_length=250 ,null=True,blank=True,verbose_name='المواد المطلوبة')
    Ord_Delivery_Instructions = models.CharField (max_length=500 ,null=True,blank=True,verbose_name='تعليمات التسليم')

    
    def __str__(self):
        return str   (self.Ord_work_order_number) 
    
   # def get_absolute_url(self):
        return reverse('order:Order_Details', kwargs={'pk': self.pk})

    def count_namber_of_Order(self):
        code = self.__class__.objects.filter(Ord_Product=self.Ord_Product).count()+1
        return "-{0:05d}".format(code)
    def count_namber_order (self) :
        code = self.__class__.objects.all().count()+1
        return str (code)
   

    def save(self, *args, **kwargs):
        if  self.id:
          self.Ord_work_order_number =  self.Ord_code_Edited 


        else:            
            self.Ord_work_order_number = self.count_namber_order()
            self.Ord_code_Edited = self.Ord_work_order_number
            
        super(Order, self).save(*args, **kwargs)
        

   # def save(self, *args, **kwargs):
       # if  self.id:
       #   self.Ord_code_pro =  self.Ord_code_pro_update         

       # else:            
        #    self.Ord_code_pro =self.Ord_Product.Product_MyCode + self.count_namber_of_Order()
        #    self.Ord_code_pro_update = self.Ord_code_pro
        #super(Order, self).save(*args, **kwargs)
    @staticmethod
    def count_new_orders():
        return Order.objects.filter(Ord_states__name='جديد').count()


    



class Paper_and_cardboard_data(models.Model):
    CARD_Work_order_number_in_chart=models.CharField(max_length=50, null=True, blank=True,verbose_name='رقم امر الشغل فى  الشيتر')
    CARD_note_Paper_type_and_size = models.CharField(max_length=50, null=True, blank=True,verbose_name='ملاحظات على نوع الورق ومقاسة')
    CARD_Cut_size = models.CharField(max_length=50, null=True, blank=True,verbose_name='مقاس قص السكينه')
    CARD_fiber_direction = models.CharField(max_length=50, null=True, blank=True,verbose_name='اتجاه الالياف')
    CARD_Total_weight = models.CharField(max_length=50, null=True, blank=True,verbose_name='العددالاجمالى')
    CARD_Order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True,verbose_name='الامر')
#--------------------main data------------------------------------------------------------------------------------------------------
    CARD_Supplier = models.CharField(max_length=50, null=True, blank=True,verbose_name='المورد',default='')
    CARD_Paper_type_and_size= models.CharField(max_length=50, null=True, blank=True,verbose_name='نوع الورق ومقاسة',default='')
    CARD_Grame = models.CharField(max_length=50, null=True, blank=True,verbose_name='جرام',default='')
    CARD_long_number = models.CharField(max_length=50, null=True, blank=True,verbose_name='عدد الطول',default='')
    CARD_Number = models.CharField(max_length=50, null=True, blank=True,verbose_name='العدد',default='')
   
    #بيانات الوزن 
    CARD_Gross_weight = models.CharField(max_length=50, null=True, blank=True,verbose_name='الوزن القائم',default='')
    CARD_Net_weight = models.CharField(max_length=50, null=True, blank=True,verbose_name='الوزن الصافى',default='')
#-------------------------------------------------------------------------------------------------------------------
#-------------------- data 1 ------------------------------------------------------------------------------------------------------
    CARD_Supplier_1 = models.CharField(max_length=50, null=True, blank=True,verbose_name='المورد',default='')
    CARD_Paper_type_and_size_1 = models.CharField(max_length=50, null=True, blank=True,verbose_name='نوع الورق ومقاسة',default='')
    CARD_Grame_1 = models.CharField(max_length=50, null=True, blank=True,verbose_name='جرام',default='')
    CARD_long_number_1 = models.CharField(max_length=50, null=True, blank=True,verbose_name='عدد الطول',default='')
    CARD_Number_1 = models.CharField(max_length=50, null=True, blank=True,verbose_name='العدد',default='')
    #بيانات الوزن 
    CARD_Gross_weight_1 = models.CharField(max_length=50, null=True, blank=True,verbose_name='الوزن القائم',default='')
    CARD_Net_weight_1 = models.CharField(max_length=50, null=True, blank=True,verbose_name='الوزن الصافى',default='')
#-------------------------------------------------------------------------------------------------------------------
#-------------------- data 2------------------------------------------------------------------------------------------------------
    CARD_Supplier_2 = models.CharField(max_length=50, null=True, blank=True,verbose_name='المورد',default='')
    CARD_Paper_type_and_size_2 = models.CharField(max_length=50, null=True, blank=True,verbose_name='نوع الورق ومقاسة',default='')
    CARD_Grame_2 = models.CharField(max_length=50, null=True, blank=True,verbose_name='جرام',default='')
    CARD_long_number_2 = models.CharField(max_length=50, null=True, blank=True,verbose_name='عدد الطول',default='')
    CARD_Number_2 = models.CharField(max_length=50, null=True, blank=True,verbose_name='العدد',default='')
    #بيانات الوزن 
    CARD_Gross_weight_2 = models.CharField(max_length=50, null=True, blank=True,verbose_name='الوزن القائم',default='')
    CARD_Net_weight_2= models.CharField(max_length=50, null=True, blank=True,verbose_name='الوزن الصافى',default='')
#-------------------------------------------------------------------------------------------------------------------
#-------------------- data 3------------------------------------------------------------------------------------------------------
    CARD_Supplier_3 = models.CharField(max_length=50, null=True, blank=True,verbose_name='المورد',default='')
    CARD_Paper_type_and_size_3 = models.CharField(max_length=50, null=True, blank=True,verbose_name='نوع الورق ومقاسة',default='')
    CARD_Grame_3 = models.CharField(max_length=50, null=True, blank=True,verbose_name='جرام',default='')
    CARD_long_number_3 = models.CharField(max_length=50, null=True, blank=True,verbose_name='عدد الطول',default='')
    CARD_Number_3 = models.CharField(max_length=50, null=True, blank=True,verbose_name='العدد',default='')
    #بيانات الوزن 
    CARD_Gross_weight_3 = models.CharField(max_length=50, null=True, blank=True,verbose_name='الوزن القائم',default='')
    CARD_Net_weight_3 = models.CharField(max_length=50, null=True, blank=True,verbose_name='الوزن الصافى',default='')
#-------------------------------------------------------------------------------------------------------------------
   


    

class Order_states(models.Model):
    FONT_CHOICES = (

    ('جديد', 'جديد'),
    ('تصميم', 'تصميم'),
    ('مونتاج', 'مونتاج'),
    ('أفلام ', 'أفلام'),
    ('سلوفان', 'سلوفان'),
    ('شراء ورق', 'شراء ورق'),
    ('ورق', 'ورق'),
    ('شيتر', 'شيتر'),
    ('تجهيز ورق', 'تجهيز ورق'),
    ('GTO(1) طباعة ربع', 'GTO(1) طباعة ربع'),
    ('SM(2) طباعة ربع', 'SM(2) طباعة ربع'),
    ('SM(5) طباعة ربع', 'SM(5) طباعة ربع'),
    ('SORM طباعة نص', 'SORM طباعة نص'),
    ('SM(2) طباعة نص', 'SM(2) طباعة نص'),
    ('SM طباعة فرخ', 'SM طباعة فرخ'),
    ('CD(5) طباعة فرخ', 'CD(5) طباعة فرخ'),
    ('سلوفان', 'سلوفان'),
    ('خدمات طباعة ورنيش/يوفي', 'خدمات طباعة ورنيش/يوفي'),
    ('خدمات طباعة خارجي', 'خدمات طباعة خارجي'),
    ('DIE 46 تكسير', 'DIE 46 تكسير'),
    ('DIE 57 تكسير', 'DIE 57 تكسير'),
    ('BOBST تكسير', 'BOBST تكسير'),
    ('التسليك و التنظيف', 'التسليك و التنظيف'),
    ('PACTEK 85 تلزيق', 'PACTEK 85 تلزيق'),
    ('PACTEK 65 تلزيق', 'PACTEK 65 تلزيق'),
    ('FG  تلزيق','FG  تلزيق' ),
    ( 'SBL  تلزيق',  'SBL  تلزيق'),
    ('تلزيق يدوي', 'تلزيق يدوي'),
    ('تجليد', 'تجليد'),
    ('قص بضاعة منتهية', 'قص بضاعة منتهية'),
    ('تلزيق خارجي', 'تلزيق خارجي'),
    ('Under Delivery', 'Under Delivery'),#NEW STATES 
    ('Closed', 'Closed'),
    ('حسابات', 'حسابات'),
    ('Invoiced', 'Invoiced'),
    ('Deleted', 'Deleted'),
    ('Finished', 'Finished')
    )
    name = models.CharField(max_length=50, null=True, blank=True,verbose_name='الاسم',choices=FONT_CHOICES) 

    def __str__(self):
        return str (self.name) 

    def get_absolute_url(self):
        return reverse('order:Order_states', kwargs={'pk': self.pk})
    
    

