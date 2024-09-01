# orders/context_processors.py
from .models import Order, Order_states

def add_variable_to_context(request):
    new_orders_count = Order.objects.filter(Ord_states__name='جديد').count()
    design_orders_count = Order.objects.filter(Ord_states__name='تصميم').count()
    montage_orders_count = Order.objects.filter(Ord_states__name='مونتاج').count()
    total_Prepress_count = new_orders_count + design_orders_count + montage_orders_count
    films_orders_count = Order.objects.filter(Ord_states__name='أفلام ').count()
    
    paper_purchase_orders_count = Order.objects.filter(Ord_states__name='شراء ورق').count()
    paper_orders_count = Order.objects.filter(Ord_states__name='ورق').count()
    sheeter_orders_count = Order.objects.filter(Ord_states__name='شيتر').count()
    total_Paper_Prepration_count = (films_orders_count  +
                                   paper_purchase_orders_count + paper_orders_count +
                                   sheeter_orders_count )
    paper_preparation_orders_count = Order.objects.filter(Ord_states__name='تجهيز ورق').count()

    gto1_print_quarter_orders_count = Order.objects.filter(Ord_states__name='GTO(1) طباعة ربع').count()
    sm2_print_quarter_orders_count = Order.objects.filter(Ord_states__name='SM(2) طباعة ربع').count()
    sm5_print_quarter_orders_count = Order.objects.filter(Ord_states__name='SM(5) طباعة ربع').count()
    sorm_print_half_orders_count = Order.objects.filter(Ord_states__name='SORM طباعة نص').count()
    sm2_print_half_orders_count = Order.objects.filter(Ord_states__name='SM(2) طباعة نص').count()
    sm_print_chick_orders_count = Order.objects.filter(Ord_states__name='SM طباعة فرخ').count()
    cd5_print_chick_orders_count = Order.objects.filter(Ord_states__name='CD(5) طباعة فرخ').count()
    total_Printing_count = (paper_preparation_orders_count + gto1_print_quarter_orders_count  +
                                   sm2_print_quarter_orders_count + sm5_print_quarter_orders_count +
                                   sorm_print_half_orders_count + sm2_print_half_orders_count +sm_print_chick_orders_count +cd5_print_chick_orders_count)
    lamination_orders_count = Order.objects.filter(Ord_states__name='سلوفان').count()
    printing_varnish_services_uv_orders_count = Order.objects.filter(Ord_states__name='خدمات طباعة ورنيش/يوفي').count()
    external_printing_services_orders_count = Order.objects.filter(Ord_states__name='خدمات طباعة خارجي').count()
    total_Printing_Services_count = (lamination_orders_count  +
                                   printing_varnish_services_uv_orders_count + external_printing_services_orders_count  )
    die_cutting_46_orders_count = Order.objects.filter(Ord_states__name='DIE 46 تكسير').count()
    die_cutting_57_orders_count = Order.objects.filter(Ord_states__name='DIE 57 تكسير').count()
    bobst_die_cutting_orders_count = Order.objects.filter(Ord_states__name='BOBST تكسير').count()
    wiring_and_cleaning_orders_count = Order.objects.filter(Ord_states__name='التسليك و التنظيف').count()
    total_Diecutting_count = (die_cutting_46_orders_count  +
                                   die_cutting_57_orders_count + bobst_die_cutting_orders_count + wiring_and_cleaning_orders_count)
    pactek_85_gluing_orders_count = Order.objects.filter(Ord_states__name='PACTEK 85 تلزيق').count()
    pactek_65_gluing_orders_count = Order.objects.filter(Ord_states__name='PACTEK 65 تلزيق').count()
    fg_gluing_orders_count = Order.objects.filter(Ord_states__name='FG تلزيق').count()
    sbl_gluing_orders_count = Order.objects.filter(Ord_states__name='SBL تلزيق').count()
    manual_gluing_orders_count = Order.objects.filter(Ord_states__name='تلزيق يدوي').count()
    binding_orders_count = Order.objects.filter(Ord_states__name='تجليد').count()
    finished_goods_cutting_orders_count = Order.objects.filter(Ord_states__name='قص بضاعة منتهية').count()
    external_gluing_orders_count = Order.objects.filter(Ord_states__name='تلزيق خارجي').count()
    total_Gluing_count = (pactek_85_gluing_orders_count  + pactek_65_gluing_orders_count + fg_gluing_orders_count + sbl_gluing_orders_count + manual_gluing_orders_count + binding_orders_count + finished_goods_cutting_orders_count + external_gluing_orders_count )
    
    
    Under_Delivery_count = Order.objects.filter(Ord_states__name='Under Delivery').count()
    closed_orders_count = Order.objects.filter(Ord_states__name='Closed').count()
    
    accounting_orders_count = Order.objects.filter(Ord_states__name='حسابات').count()
    
    deleted_orders_count = Order.objects.filter(Ord_states__name='Deleted').count()
    finished_orders_count = Order.objects.filter(Ord_states__name='Finished').count()
    
    total_orders_count=(total_Prepress_count+total_Paper_Prepration_count+total_Printing_count+total_Printing_Services_count+total_Diecutting_count+total_Gluing_count)
    

    return {
        'new_orders_count': new_orders_count,
        'design_orders_count': design_orders_count,
        'montage_orders_count': montage_orders_count,
        'total_Prepress_count': total_Prepress_count,
        'films_orders_count': films_orders_count,
        'lamination_orders_count': lamination_orders_count,
        'paper_purchase_orders_count': paper_purchase_orders_count,
        'paper_orders_count': paper_orders_count,
        'sheeter_orders_count': sheeter_orders_count,
        'paper_preparation_orders_count': paper_preparation_orders_count,
        'total_Paper_Prepration_count': total_Paper_Prepration_count,
        'gto1_print_quarter_orders_count': gto1_print_quarter_orders_count,
        'sm2_print_quarter_orders_count': sm2_print_quarter_orders_count,
        'sm5_print_quarter_orders_count': sm5_print_quarter_orders_count,
        'sorm_print_half_orders_count': sorm_print_half_orders_count,
        'sm2_print_half_orders_count': sm2_print_half_orders_count,
        'sm_print_chick_orders_count': sm_print_chick_orders_count,
        'cd5_print_chick_orders_count': cd5_print_chick_orders_count,
        'total_Printing_count': total_Printing_count,
        'printing_varnish_services_uv_orders_count': printing_varnish_services_uv_orders_count,
        'external_printing_services_orders_count': external_printing_services_orders_count,
        'total_Printing_Services_count': total_Printing_Services_count,
        'die_cutting_46_orders_count': die_cutting_46_orders_count,
        'die_cutting_57_orders_count': die_cutting_57_orders_count,
        'bobst_die_cutting_orders_count': bobst_die_cutting_orders_count,
        'wiring_and_cleaning_orders_count': wiring_and_cleaning_orders_count,
        'total_Diecutting_count': total_Diecutting_count,
        'pactek_85_gluing_orders_count': pactek_85_gluing_orders_count,
        'pactek_65_gluing_orders_count': pactek_65_gluing_orders_count,
        'fg_gluing_orders_count': fg_gluing_orders_count,
        'sbl_gluing_orders_count': sbl_gluing_orders_count,
        'manual_gluing_orders_count': manual_gluing_orders_count,
        'binding_orders_count': binding_orders_count,
        'finished_goods_cutting_orders_count': finished_goods_cutting_orders_count,
        'external_gluing_orders_count': external_gluing_orders_count,
        'total_Gluing_count': total_Gluing_count,
        'Under_Delivery_count': Under_Delivery_count,
        'closed_orders_count': closed_orders_count,
        'accounting_orders_count': accounting_orders_count,

        'deleted_orders_count': deleted_orders_count,
        'finished_orders_count': finished_orders_count,
        'total_orders_count': total_orders_count
    }
