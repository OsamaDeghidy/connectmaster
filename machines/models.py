from django.db import models
from Order.models import Order


# Create your models here.


class Machine(models.Model):
    machine_CHOICES = (  
#printing 
    ('تجهيز ورق', 'تجهيز ورق'),
    ('GTO(1) طباعة ربع', 'GTO(1) طباعة ربع'),
    ('SM(2) طباعة ربع', 'SM(2) طباعة ربع'),
    ('SM(5) طباعة ربع', 'SM(5) طباعة ربع'),
    ('SORM طباعة نص', 'SORM طباعة نص'),
    ('SM(2) طباعة نص', 'SM(2) طباعة نص'),
    ('SM طباعة فرخ', 'SM طباعة فرخ'),
    ('CD(5) طباعة فرخ', 'CD(5) طباعة فرخ'),
 #printing serveirs
    ('سلوفان', 'سلوفان'),
    ('خدمات طباعة ورنيش/يوفي', 'خدمات طباعة ورنيش/يوفي'),
    ('خدمات طباعة خارجي', 'خدمات طباعة خارجي'),
    #deicutting 
     ('DIE 46 تكسير', 'DIE 46 تكسير'),
    ('DIE 57 تكسير', 'DIE 57 تكسير'),
    ('BOBST تكسير', 'BOBST تكسير'),
    ('التسليك و التنظيف', 'التسليك و التنظيف'),
    #gluing
   
    ('PACTEK 85 تلزيق', 'PACTEK 85 تلزيق'),
    ('PACTEK 65 تلزيق', 'PACTEK 65 تلزيق'),
    ('FG  تلزيق','FG  تلزيق' ),
    ( 'SBL  تلزيق',  'SBL  تلزيق'),
    ('تلزيق يدوي', 'تلزيق يدوي'),
    ('تجليد', 'تجليد'),
    ('قص بضاعة منتهية', 'قص بضاعة منتهية'),
    ('تلزيق خارجي', 'تلزيق خارجي'),
    
   
    )
    machine_name = models.CharField(max_length=200, unique=True, null=True, blank=True,choices=machine_CHOICES)
    machine_code = models.CharField(max_length=200, unique=True, null=True, blank=True)
  
    def __str__(self):
        return str(self.machine_name)



class Machine_Order(models.Model):
    machine = models.ManyToManyField(Machine)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    
    paper_processing = models.PositiveIntegerField(blank=True, null=True, verbose_name='تجهيز ورق')
    gto1_print_quarter = models.PositiveIntegerField(blank=True, null=True, verbose_name='GTO(1) طباعة ربع')
    sm2_print_quarter = models.PositiveIntegerField(blank=True, null=True, verbose_name='SM(2) طباعة ربع')
    sm5_print_quarter = models.PositiveIntegerField(blank=True, null=True, verbose_name='SM(5) طباعة ربع')
    sorm_print_half = models.PositiveIntegerField(blank=True, null=True, verbose_name='SORM طباعة نص')
    sm2_print_half = models.PositiveIntegerField(blank=True, null=True, verbose_name='SM(2) طباعة نص')
    sm_print_chick = models.PositiveIntegerField(blank=True, null=True, verbose_name='SM طباعة فرخ')
    cd5_print_chick = models.PositiveIntegerField(blank=True, null=True, verbose_name='CD(5) طباعة فرخ')
    lamination = models.PositiveIntegerField(blank=True, null=True, verbose_name='سلوفان')
    printing_varnish_services_uv = models.PositiveIntegerField(blank=True, null=True, verbose_name='خدمات طباعة ورنيش/يوفي')
    external_printing_services = models.PositiveIntegerField(blank=True, null=True, verbose_name='خدمات طباعة خارجي')
    die_cutting_46 = models.PositiveIntegerField(blank=True, null=True, verbose_name='DIE 46 تكسير')
    die_cutting_57 = models.PositiveIntegerField(blank=True, null=True, verbose_name='DIE 57 تكسير')
    bobst_die_cutting = models.PositiveIntegerField(blank=True, null=True, verbose_name='BOBST تكسير')
    wiring_and_cleaning = models.PositiveIntegerField(blank=True, null=True, verbose_name='التسليك و التنظيف')
    pactek_85_gluing = models.PositiveIntegerField(blank=True, null=True, verbose_name='PACTEK 85 تلزيق')
    pactek_65_gluing = models.PositiveIntegerField(blank=True, null=True, verbose_name='PACTEK 65 تلزيق')
    fg_gluing = models.PositiveIntegerField(blank=True, null=True, verbose_name='FG  تلزيق')
    sbl_gluing = models.PositiveIntegerField(blank=True, null=True, verbose_name='SBL  تلزيق')
    manual_gluing = models.PositiveIntegerField(blank=True, null=True, verbose_name='تلزيق يدوي')
    binding = models.PositiveIntegerField(blank=True, null=True, verbose_name='تجليد')
    finished_goods_cutting = models.PositiveIntegerField(blank=True, null=True, verbose_name='قص بضاعة منتهية')
    external_gluing = models.PositiveIntegerField(blank=True, null=True, verbose_name='تلزيق خارجي')
    
    def __str__(self):
        machines = ", ".join([str(m) for m in self.machine.all()])
        return f"{machines}-- {self.order}"
    
    
