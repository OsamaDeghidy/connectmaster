from datetime import timezone
import functools
from django.db import models
#import sum
from django.db.models import Sum
#import user
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.db.models.signals import post_save

from django.dispatch import receiver
from django.forms import ValidationError

# Create your models here.
#Main_categorey-Sub_categorey-Degree
class Main_categorey(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    #code 
    def  code_Main_categorey   (self):
        return self.code  

class Sub_categorey(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    main_categorey = models.ForeignKey(Main_categorey, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    #code
    def  code_Sub_categorey   (self):
        return self.code

class Peper_type_country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    #code
    def  code_Peper_type_country   (self):
        return self.code


class Degree(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    def __str__(self):
        return self.name   
    #code
    def  code_Degree   (self):
        return self.code     




class Gram_Categore (models.Model):
    name = models.FloatField(max_length=100,default=0000)
    code = models.CharField(max_length=3,default=0000)
    def __str__(self):
        return str (self.name)   
        #code
    def  code_Gram_Categore   (self):   
        return str (self.name)

class linght (models.Model):
    name = models.FloatField(max_length=100 ,default=0000)
    code = models.CharField(max_length=4, default=0000 )
    def __str__(self):
        return str (self.name)   
    #code
    def  code_linght   (self):   
        return str (self.name)   

class width (models.Model):
    name = models.FloatField(max_length=100,default=0000)
    code = models.CharField(max_length=4,default=0000)
    def __str__(self):
        return str (self.name)   
    #code
    def  code_width   (self):   
        return str (self.name)


#المورديدن
class Supplier(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='الاسم')
    address = models.CharField(max_length=100 , verbose_name='العنوان')
    phone = models.CharField(max_length=100 , verbose_name='الهاتف')
    email = models.EmailField(max_length=100 , verbose_name='الايميل')
    def __str__(self):
        return str (self.name) 


#الاصناف
class Iteam (models.Model):# iteam 
    code = models.CharField(max_length=100, verbose_name='الكود',default='00-00-00-00-000',  )
    name = models.CharField(max_length=100, verbose_name='الاسم',default='الاسم الكامل للصنف ', )
    main_categorey = models.ForeignKey(Main_categorey, on_delete=models.CASCADE, null=True, blank=True)
    sub_categorey = models.ForeignKey(Sub_categorey, on_delete=models.CASCADE, null=True, blank=True)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, null=True, blank=True)
    peper_type_country = models.ForeignKey(Peper_type_country, on_delete=models.CASCADE, null=True, blank=True)
    gram_categore = models.IntegerField(default='000')
    linght = models.IntegerField(default='0000')
    width = models.IntegerField(default='0000')
    #الكميه
    
    def __str__(self):
        return str (self.name) 

    


  
        
        
    
@receiver(pre_save, sender=Iteam)
def set_iteam_code_and_name(sender, instance, **kwargs):
    instance.code = f"{instance.main_categorey.code}-{instance.sub_categorey.code}-{instance.degree.code}-{instance.peper_type_country.code}-{instance.gram_categore}{instance.linght}{instance.width}"
    instance.name = f"{instance.main_categorey.name} {instance.sub_categorey.name} {instance.degree.name} {instance.peper_type_country.name} {instance.gram_categore} {instance.linght} {instance.width}"



class InStockNumber(models.Model):
    STATUS = (
        ('تعديل', 'تعديل'),
        ('نهائي', 'نهائي'),
       )
    date=models.DateField(auto_now_add=True,verbose_name='التاريخ')
    number = models.IntegerField(default=0,verbose_name='رقم امر التوريد ')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,verbose_name='المورد')
    status = models.CharField(max_length=100, verbose_name='الحاله',default='تعديل' ,choices=STATUS)
    def __str__(self):
        return str (self.number)

@receiver(post_save, sender=InStockNumber)
def update_instocknumber_count(sender, instance, created, **kwargs):
    if created:
        instance.number = InStockNumber.objects.count()
        instance.save() 

    


#اذن التوريد
class In_stock(models.Model): 
    date = models.DateField(auto_now_add=True,verbose_name='التاريخ',null=True, blank=True)
    in_stocknumber = models.ForeignKey(InStockNumber, on_delete=models.CASCADE,verbose_name='رقم امر التوريد')
    iteam = models.ForeignKey(Iteam, on_delete=models.CASCADE,verbose_name='الصنف')
    weaight = models.FloatField(max_length=100, verbose_name='الوزن',default=0,null=True, blank=True)
    sheet = models.IntegerField(default=0,null=True, blank=True,verbose_name='الورقه')
    price = models.FloatField(max_length=100, verbose_name='السعر',default=0,null=True, blank=True)
    name=models.CharField(max_length=100, verbose_name='الاسم',default='اذن توريد')
    code=models.CharField(max_length=100, verbose_name='الكود',default='00-00-00-00-000000000000-0000', )
    



    def __str__(self):
        return str (self.name)
    def save(self, *args, **kwargs):
     if self.weaight is not None and self.iteam.main_categorey.code != '01':
        self.sheet = (self.weaight * 10**9) / (self.iteam.linght * self.iteam.width * self.iteam.gram_categore)
     elif self.sheet is not None and self.iteam.main_categorey.code != '01':
        self.weaight = (self.sheet * self.iteam.linght * self.iteam.width * self.iteam.gram_categore) / 10**9

     super().save(*args, **kwargs)
   

   
   
   

@receiver(pre_save, sender=In_stock)
def set_In_stoke_code(sender, instance, **kwargs):
  if instance.iteam:
    similar_items = In_stock.objects.filter(
        iteam=instance.iteam.id  
    )
    counter = similar_items.count()+1
    instance.code = f"{instance.iteam.code}-{str(counter).zfill(4)}"
    instance.name = f"{instance.iteam.name}-{str(counter).zfill(4)}"
  else:
        # Handle the case where iteam is not set
        pass



#العميل        
class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='الاسم')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, verbose_name='العنوان')
    phone = models.CharField(max_length=100, verbose_name='الهاتف')
    email = models.EmailField(max_length=100, verbose_name='الايميل')
   

    def __str__(self):
        return str (self.name)


# اذن صرف الريسى    
class Out_StockNumber(models.Model):
    STATUS = (
        ('تعديل', 'تعديل'),
        ('نهائي', 'نهائي'),
    )
    date = models.DateField(auto_now_add=True,null=True, blank=True,verbose_name='التاريخ')
    number = models.IntegerField(default=0,verbose_name='رقم امر الصرف ')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name='العميل')
    status = models.CharField(max_length=100, verbose_name='الحاله',default='تعديل' ,choices=STATUS)
    def __str__(self):
        return str (self.number)

@receiver(post_save, sender=Out_StockNumber)
def update_outstocknumber_count(sender, instance, created, **kwargs):
    if created:
        instance.number = Out_StockNumber.objects.count()
        instance.save()
    
#اذن صرف 
class  Out_Stock(models.Model):
    date = models.DateField(auto_now_add=True,null=True, blank=True,verbose_name='التاريخ')
    iteam=models.ForeignKey(Iteam, on_delete=models.CASCADE,verbose_name='الصنف',null=True, blank=True)
    out_stocknumber = models.ForeignKey(Out_StockNumber, on_delete=models.CASCADE,verbose_name='رقم امر الصرف')
    in_stock= models.ForeignKey(In_stock, on_delete=models.CASCADE,verbose_name='الصنف')
    weaight = models.FloatField(max_length=100, verbose_name='الوزن',default=0,null=True, blank=True)
    sheet = models.IntegerField(default=0,null=True, blank=True,verbose_name='الشيت')
    price = models.FloatField(max_length=100, verbose_name='السعر',default=0,null=True, blank=True)
                          
   
    def __str__(self):
        return str (self.in_stock.name)
    
    def save(self, *args, **kwargs):
        if self.weaight is not None and self.iteam.main_categorey.code != '01':
            self.sheet = (self.weaight * 10**9) / (self.iteam.linght * self.iteam.width * self.iteam.gram_categore)
        elif self.sheet is not None and self.iteam.main_categorey.code != '01':
            self.weaight = (self.sheet * self.iteam.linght * self.iteam.width * self.iteam.gram_categore) / 10**9
    
        super().save(*args, **kwargs)




















#removed
class In_stoke_detals (models.Model):
    date = models.DateField(auto_now_add=True)
#البكر #removed
class Pukker (models.Model):  
    weaight = models.FloatField(default=0, null=True, blank=True)
#البكر الواباكو  #removed
class Sub (models.Model):
    weaight = models.FloatField(default=0, null=True, blank=True)

   
 

    

#removed
class Pako (models.Model):
    weaight = models.FloatField(default=0, null=True, blank=True)
    
  



   