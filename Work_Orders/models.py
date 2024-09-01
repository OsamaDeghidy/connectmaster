from itertools import count
import secrets
from tabnanny import verbose

from django.db import models
from django.contrib.auth.models import User


from multiselectfield import MultiSelectField
from Order.models import Order


# Sectors Table
class Sector(models.Model):
    Sector_Name = models.CharField(max_length=50,unique=True)
    Sector_Code = models.CharField(max_length=2,unique=True)
    Sector_Description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.Sector_Name)


    
        
    def save_sector(self,*args,**kwargs):
        self.Sector_Code = self.Sector_Name[:2].upper() 
        super().save(*args,**kwargs)


    def get_products_count(self):
        return Product.objects.filter(Product_Customer__Customer_Sector=self).count()
    
    def get_orders_count(self):
        return Order.objects.filter(Ord_Product__Product_Customer__Customer_Sector=self).count()

    def get_last_customer(self):
         return Customer.objects.filter(Customer_Sector__Sector_Name=self).order_by('Created_Dt').last()  #returns the last customer created
    

class Representative(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name    

# Customers Table
class Customer(models.Model):
    Customer_Name = models.CharField(max_length=200,unique=True)
    customer_code =models.CharField(max_length=9,unique=True)
    Customer_Sector = models.ForeignKey(Sector,related_name='Customers',on_delete=models.CASCADE)
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE,blank=True,null=True,default=None)
    Created_By = models.ForeignKey(User,related_name='Customers',on_delete=models.CASCADE)
    Created_Dt = models.DateField(auto_now_add=True)
    Contact_Name = models.CharField(max_length=200,blank=True,null=True)
    Contact_Phone = models.CharField(max_length=50,blank=True,null=True)
    Contact_Email = models.EmailField(max_length=254,blank=True,null=True)
    Customer_code_edite=models.CharField(max_length=20,editable=False,blank=True,null=True)


    def __str__ (self):
        return str(self.Customer_Name)

#def save(self, *args, **kwargs):
   # self.customer_code =  self.Customer_Sector.Sector_Code + self.count_nember_sector()


   # super().save(*args, **kwargs)
        
    
    def save(self, *args, **kwargs):
         
         if  self.id: # new object, so set slug
             self.customer_code = self.Customer_code_edite

         else: # existing object, so ignore slug
             self.customer_code = self.Customer_Sector.Sector_Code + self.count_nember_sector()
             self.Customer_code_edite = self.customer_code 
         super().save(*args, **kwargs)

    def get_products_count(self):
       return Product.objects.filter(Product_Customer__Customer_Name=self).count()
    def get_orders_count(self): 
       return Order.objects.filter(Ord_Product__Product_Customer__Customer_Name=self).count()
    def get_last_order(self): 
       return Order.objects.filter(Order_Product__Product_Customer__Customer_Name=self).order_by('-Created_Dt').first()
    def count_nember_sector(self):
       code=self.__class__.objects.filter(Customer_Sector=self.Customer_Sector).count()+1
       return "-{:02}".format(code)
      

    def get_last_product(self):
       return Product.objects.filter(Product_Customer__Customer_Name=self).order_by('-Created_Dt').first()  #returns the last product created       

    

        

   


# Account Table
class Account(models.Model):
    Account_Customer =  models.ForeignKey(Customer,related_name='Accounts',on_delete=models.CASCADE)
    Account_Manager = models.ForeignKey(User,related_name='Accounts',on_delete=models.CASCADE)

# Products Table
class Product(models.Model):
    STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Deleted', 'Deleted'),)
    Product_Name = models.CharField(max_length=300,verbose_name=('اسم النتج'))
    Product_Code = models.CharField(max_length=50,verbose_name=('كود العميل'),blank=True,null=True)
    product_Ordered_Supply=models.CharField(max_length=50,verbose_name=('أمر توريد'),blank=True,null=True)
    customer_representative = models.CharField (choices=[('د/عمروالباز','د/عمروالباز'),('ا/عمرو احمد','ا/عمرو احمد'),('م/كريم عبد الغنى','م/كريم عبد الغنى'),('أخرى','أخرى')],max_length=100,verbose_name=('ممثل  العميل'),default= 'أخرى')
    product_dicription=models.ForeignKey("Product_Dicription",related_name='Product_Description',blank=True ,null=True,on_delete=models.CASCADE ,verbose_name=('وصف المنتج'))
    Product_length = models.FloatField(blank=True,null=True)
    Product_width = models.FloatField(blank=True,null=True)
    Product_height = models.FloatField(blank=True,null=True)
    product_avrage_prdect_ammount = models.CharField(default=0,verbose_name=('المتوسط'),blank=True,null=True,max_length=20)
    Product_Allowable_increase=MultiSelectField(choices=(('حسب أمر الشغل','حسب أمر الشغل'),('10% بحد أقصى','10% بحد أقصى')),max_length=50,default='حسب امر الشغل ',verbose_name=('*الزيادة المسموح بها  '))
    Product_Design_and_printing_specifications=models.ForeignKey("Design_And_Printing_Specifications",related_name='Products',blank=True,on_delete=models.CASCADE ,null=True)
    Product_paper_specification = models.ForeignKey("Paper_Specification",related_name='Products',blank=True,on_delete=models.CASCADE ,null=True)
    Product_Aftar_Print_Services = models.ForeignKey("Aftar_Print_Services",related_name='Products',blank=True,on_delete=models.CASCADE ,null=True)
    Product_Crushing_Data=models.ForeignKey("Crushing_Data",related_name='Products',blank=True,on_delete=models.CASCADE ,null=True)
    Product_Gluing_And_Binding_Data=models.ForeignKey("Gluing_And_Binding_Data",related_name='Products',blank=True,on_delete=models.CASCADE ,null=True)
    Product_Finished_product_and_packing_data=models.ForeignKey("Finished_product_and_packing_data",related_name='Products',blank=True,on_delete=models.CASCADE ,null=True)
    #Product_CorrectiveActions=models.ForeignKey("CorrectiveActions",related_name='Products',blank=True,on_delete=models.CASCADE ,null=True) # اجراءات تصصيصيه المنتجات

    Product_MyCode=models.CharField(max_length=50,unique=True)
    Product_Customer = models.ForeignKey(Customer,related_name='Products',on_delete=models.CASCADE)
    Product_Sector = models.ForeignKey(Sector,related_name='Products',on_delete=models.CASCADE)
    Created_By = models.ForeignKey(User,related_name='Products',on_delete=models.CASCADE)
    Created_Dt = models.DateField(auto_now_add=True)
    Product_status = models.CharField(max_length=50, null=True, blank=True, default="Active" ,choices=STATUS_CHOICES) #, choices=STATUS_CHOICES
    Product_Details = models.TextField(max_length=4000,null=True, blank=True,)


    
  
    # Product_Codew
    # Product_Version
    # Product_Attachement

    def __str__ (self):
        return str(self.Product_MyCode)

    def save(self, *args, **kwargs):
        if not self.id:  # Check if the product is being created for the first time
            gg = self.Product_Customer.customer_code
            code = self.__class__.objects.filter(Product_Customer=self.Product_Customer).count() + 1
            self.Product_MyCode = "{}-{:04d}".format(gg, code)
        else:
            # If the product already exists, keep the existing Product_MyCode
            existing_product = self.__class__.objects.get(id=self.id)
            self.Product_MyCode = existing_product.Product_MyCode

        super(Product, self).save(*args, **kwargs)

    def get_orders_count(self): 
       return Order.objects.filter(Ord_Product=self).count()

class Design_And_Printing_Specifications(models.Model):
    pro_design_source=MultiSelectField(choices=(('المطبعة','المطبعة'),('العميل','العميل')),max_length=20,verbose_name=('مصدر التصميم '),blank=True,null=True,default=None) #if the design is from the printer or from the customer
    pro_design_type=MultiSelectField(choices=(('جديد','جديد'),('تعديل','تعديل'),('قديم','قديم')),max_length=70,verbose_name=('نوع التصميم '),blank=True,null=True,default=None)
    pro_design_ditals=models.CharField(max_length=1000,verbose_name=('تفاصيل التصميم '),blank=True,null=True,default=None)
    pro_old_execution=MultiSelectField(choices=([('إعدام القديم','إعدام القديم')]),max_length=70,verbose_name=(''), blank=True,null=True,default=None)
    number_of_sides=models.CharField(choices=[('وجه','وجه'),('وجهين','وجهين'),('قلاب','قلاب')],max_length=10,default='وجه',verbose_name=('عدد الأوجه '))
    attachments_file = models.FileField(upload_to='attachments/%Y/%m/%d', blank=True, null=True, verbose_name=('إرفاق ملف معتمد  '))
    approved_montage_size = models.CharField(max_length=50, verbose_name="مقاس المونتاج المعتمد", blank=True, null=True)#مقاس المونتاج المعتمد
    approved_montage_count = models.CharField(verbose_name="العدد في المونتاج المعتمد", blank=True, null=True, max_length=50)#العدد في المونتاج المعتمد

    product_color = MultiSelectField(choices=([('Cyan','C'),('Magenta','M'),('yellow','Y'),('Key','K')]),max_length=50,blank=True,null=True,default=None ,verbose_name=('الألون'))
    tinted_colors1 = models.CharField(max_length=20, blank=True, null=True, default=None)
    tinted_colors2 = models.CharField(max_length=20, blank=True, null=True, default=None)
    tinted_colors3 = models.CharField(max_length=20, blank=True, null=True, default=None)
    tinted_colors4 = models.CharField(max_length=20, blank=True, null=True, default=None)
    tinted_colors5 = models.CharField(max_length=20, blank=True, null=True, default=None)
    tinted_colors6 = models.CharField(max_length=20, blank=True, null=True, default=None)
   
   

    def __str__ (self):
        return str(self.pro_design_source) + " " + str(self.pro_design_type)

class Pro_Paper_Type(models.Model):
    pro_paper_type=models.CharField(max_length=80)
    def __str__ (self):
        return str(self.pro_paper_type)
class Paper_Specification (models.Model):
    pro_paper_type=models.ForeignKey(Pro_Paper_Type,related_name='Paper_Specification',blank=True,null=True,on_delete=models.CASCADE,verbose_name=('نوع الورق '))
    pro_paper_gram=models.CharField(max_length=80,blank=True,null=True,default=None)
    fiber_direction=models.CharField(choices=(('ضرورية','ضرورية'),('غير ضرورىة','غير ضرورىة')),max_length=80,blank=True,null=True,default=None,verbose_name=('إتجاه الألياف '))
     
    def __str__ (self):
        return  str(self.pro_paper_gram)
class Aftar_Print_Services (models.Model):
    pro_aftar_print_services_type=MultiSelectField(choices=(('قص','قص'),('ورنيش','ورنيش'),('يوفى','يوفى'),('سلوفان','سلوفان'),('سبوت يوفى','سبوت يوفى'),('بصمة','بصمة'),('مضلع','مضلع')),max_length=100,verbose_name=('نوع الخدمة'),blank=True,null=True,default=None)
    pro_aftar_print_services_detals=models.CharField(max_length=100,blank=True,null=True,default=None)
    def __str__ (self):
        return str(self.pro_aftar_print_services_type)


class Crushing_Data (models.Model):
    pro_crushing_data_type=MultiSelectField(choices=([('تام','تام'),('شباك','شباك'),('كوفراج','كوفراج'),('ريجة','ريجة'),('فورمة','فورمة')]),max_length=100,blank=True,null=True,verbose_name=('نوع الخدمة '))
    pro_crushing_data_detals=models.CharField(max_length=100,blank=True,null=True)
    def __str__ (self):
        return str(self.pro_crushing_data_type)+" "+str(self.pro_crushing_data_detals) 

class Gluing_And_Binding_Data (models.Model):
    pro_Gluing_And_Binding_Data_type=MultiSelectField(choices=([('تلزيق آلى','تلزيق آلى'),('تلزيق يدوي','تلزيق يدوي'),('تلزيق إستالون','تلزيق إستالون'),('تجليد','تجليد')]),max_length=100,blank=True,null=True,verbose_name=('نوع الخدمة '))
    pro_Gluing_And_Binding_Data_detals=models.CharField(max_length=100,blank=True,null=True)
    def __str__ (self):
        return str(self.pro_Gluing_And_Binding_Data_type) + " " + str(self.pro_Gluing_And_Binding_Data_detals)

class Finished_product_and_packing_data (models.Model):
    pro_finished_product_and_packing_data_type=models.CharField(choices=[('باندات ورق','باندات ورق'),('أستيك','أستيك')],max_length=30,blank=True,null=True,verbose_name=('المنتج النهائي '))
    pro_Finished_product_and_packing_data_Baku=models.CharField(choices=[('ورق','ورق'),('أكياس','أكياس'),('شرنك','شرنك')],max_length=100,blank=True,null=True,verbose_name=('الباكو'))
    pro_finished_product_and_packing_data_detals=models.CharField(max_length=100,blank=True,null=True)
    def __str__ (self):
        return str(self.pro_finished_product_and_packing_data_type)  + " " + str(self.pro_Finished_product_and_packing_data_Baku) + " " + str(self.pro_finished_product_and_packing_data_detals)    

class Product_Dicription(models.Model):
    Product_Description_type = models.TextField(max_length=4000)

  
    def __str__ (self):
        return str(self.Product_Description_type)




class CorrectiveActions(models.Model): # اجراءات تصصيصيه المنتجات
    ACTIONS_CHOICES = (
        ('قيد التنفيذ', 'قيد التنفيذ'),
        ('تم التنفيذ', 'تم التنفيذ'),
        ('مرفوض', 'مرفوض'),
        ('تحت الاعتماد', 'تحت الاعتماد'),
    )

    date = models.DateField(verbose_name="التاريخ", blank=True, null=True)
    complaint_details = models.TextField(verbose_name="تفاصيل الشكوى", blank=True, null=True)
    proposed_solution = models.TextField(verbose_name="الحل المقترح", blank=True, null=True)
    product=models.ForeignKey("Product",related_name='Products',blank=True,on_delete=models.CASCADE ,null=True) # اجراءات تصصيصيه المنتجات

    action_status = models.CharField(max_length=50, choices=ACTIONS_CHOICES, verbose_name="حالة الإجراء", default='قيد التنفيذ', blank=True, null=True)
    solution = models.TextField(verbose_name="الحل", blank=True, null=True)
    
    
    class Meta:
        verbose_name = "جدول الإجراءات التصحيحية"
        verbose_name_plural = "جدول الإجراءات التصحيحية"

    def __str__(self):
        return f"{self.date} - {self.complaint_details}"
