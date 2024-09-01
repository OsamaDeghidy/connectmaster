from django.urls import path
from . import views
from .views import machine_filter_view  # تأكد من أنك تستورد الدالة من ملف views



urlpatterns = [
    path('machine/<int:order_id>/edit/', views.machineorder_edite, name='machine_edit'),
   
   


    # urls.py


    path('GTO/', views.GTO_view, name='GTO_view'),
    path('SM2/', views.SM2_view, name='SM2_view'),
    path('SM5/', views.SM5_view, name='SM5_view'),
    path('SORM/', views.SORM_view, name='SORM_view'),
    path('SM2_half/', views.SM2_half_view, name='SM2_half_view'),
    path('SM_full/', views.SM_full_view, name='SM_full_view'),
    path('CD5/', views.CD5_view, name='CD5_view'),
    path('lamination/', lambda request: views.machine_filter_view(request, 'سلوفان'), name='lamination_view'),
    path('printing_varnish_services_uv/', lambda request: views.machine_filter_view(request, 'خدمات طباعة ورنيش/يوفي'), name='printing_varnish_services_uv'),
    path('external_printing_services/', lambda request: machine_filter_view(request, 'خدمات طباعة خارجي'), name='external_printing_services'),
    path('die_cutting_46/', lambda request: machine_filter_view(request, 'DIE 46 تكسير'), name='die_cutting_46'),
    path('die_cutting_57/', lambda request: machine_filter_view(request, 'DIE 57 تكسير'), name='die_cutting_57'),
    path('bobst_cutting/', lambda request: machine_filter_view(request, 'BOBST تكسير'), name='bobst_cutting'),
    path('desilking_and_cleaning/', lambda request: machine_filter_view(request, 'التسليك و التنظيف'), name='desilking_and_cleaning'),
    path('pactek_85_gluing/', lambda request: machine_filter_view(request, 'PACTEK 85 تلزيق'), name='pactek_85_gluing'),
    path('pactek_65_gluing/', lambda request: machine_filter_view(request, 'PACTEK 65 تلزيق'), name='pactek_65_gluing'),
    path('fg_gluing/', lambda request: machine_filter_view(request, 'FG  تلزيق'), name='fg_gluing'),
    path('sbl_gluing/', lambda request: machine_filter_view(request, 'SBL  تلزيق'), name='sbl_gluing'),
    path('manual_gluing/', lambda request: machine_filter_view(request, 'تلزيق يدوي'), name='manual_gluing'),
    path('binding/', lambda request: machine_filter_view(request, 'تجليد'), name='binding'),
    path('finished_goods_cutting/', lambda request: machine_filter_view(request, 'قص بضاعة منتهية'), name='finished_goods_cutting'),
    path('external_gluing/', lambda request: machine_filter_view(request, 'تلزيق خارجي'), name='external_gluing'),
    # يمكنك إضافة المزيد من الـ URL patterns هنا
]



    
    

    
    


