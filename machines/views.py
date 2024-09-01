from audioop import reverse
import django.shortcuts


from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponseRedirect

from Order.models import Order
from .models import Machine, Machine_Order

from .forms import MachineForm, Machine_OrderForm
from django.db.models import Q
from .models import Machine_Order


def machineorder_edite(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    machine_order, _ = Machine_Order.objects.get_or_create(order=order)
    
    if request.method == 'POST':
        form = Machine_OrderForm(request.POST, instance=machine_order)
        if form.is_valid():
            form.save()  # حفظ البيانات في قاعدة البيانات
            return redirect('orders')
    else:
        form = Machine_OrderForm(instance=machine_order)
    
    return render(request, 'machines/machine_edit.html', {'form': form})



# views.py



def machine_view(request, machine_name, template_name):
    filtered_machines = [machine_name]
    machines = Machine_Order.objects.filter(machine__machine_name__in=filtered_machines).distinct()
    
    design = machines.filter(order__Ord_states__name__contains='تصميم').order_by('-id')
    produced_by = machines.filter(order__Ord_states__name__contains='مونتاج').order_by('-id')
    aflam = machines.filter(order__Ord_states__name__contains='أفلام').order_by('-id')
    
    buy_paper = machines.filter(order__Ord_states__name__contains='شراء ورق').order_by('-id')
    paper = machines.filter(order__Ord_states__name__contains='ورق').exclude(order__Ord_states__name__contains='تجهيز ورق').exclude(order__Ord_states__name__contains='شراء ورق').order_by('-id')
    chitter = machines.filter(order__Ord_states__name__contains='شيتر').order_by('-id')
    paper_processing = machines.filter(order__Ord_states__name__contains='تجهيز ورق').order_by('-id')

    Gto = machines.filter(order__Ord_states__name__contains=machine_name).order_by('-id')
    
    context = {
        'machine_name': machine_name, 
        'design': design,
        'produced_by': produced_by,
        'aflam': aflam,
        'buy_paper': buy_paper,
        'paper': paper,
        'chitter': chitter,
        'paper_processing': paper_processing,
        'Gto': Gto,
    }
    return render(request, template_name, context)



from django.http import HttpResponseForbidden

def allow_volt_only(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.username == "volt":
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not allowed to view this page.")
    return _wrapped_view_func


@allow_volt_only
def GTO_view(request):
    return machine_view(request, 'GTO(1) طباعة ربع', 'machinfilter/printing.html')

@allow_volt_only
def SM2_view(request):
    return machine_view(request, 'SM(2) طباعة ربع', 'machinfilter/printing.html')


def SORM_view(request):
    if request.user.username == "volt":
        return HttpResponseForbidden("You are not allowed to view this page.")
    return machine_view(request, 'SORM طباعة نص', 'machinfilter/printing.html')

def SM2_half_view(request):
    if request.user.username == "volt":
        return HttpResponseForbidden("You are not allowed to view this page.")
    return machine_view(request, 'SM(2) طباعة نص', 'machinfilter/printing.html')

def SM_full_view(request):
    if request.user.username == "volt":
        return HttpResponseForbidden("You are not allowed to view this page.")
    return machine_view(request, 'SM طباعة فرخ', 'machinfilter/printing.html')


# Create specific views by passing appropriate parameters
# def GTO_view(request):
#     return machine_view(request, 'GTO(1) طباعة ربع', 'machinfilter/printing.html')

# def SM2_view(request):
#     return machine_view(request, 'SM(2) طباعة ربع', 'machinfilter/printing.html')

def SM5_view(request):
     return machine_view(request, 'SM(5) طباعة ربع', 'machinfilter/printing.html')

# def SORM_view(request):
#     return machine_view(request, 'SORM طباعة نص', 'machinfilter/printing.html')

# def SM2_half_view(request):
#     return machine_view(request, 'SM(2) طباعة نص', 'machinfilter/printing.html')

# def SM_full_view(request):
#     return machine_view(request, 'SM طباعة فرخ', 'machinfilter/printing.html')
def CD5_view(request):
     return machine_view(request, 'CD(5) طباعة فرخ', 'machinfilter/printing.html')



# دالة لإنشاء فلتر بناءً على المراحل
def get_filtered_order_query(stages, exclude_stage):
    filtered_order_query = Q()
    
    for stage in stages:
        if stage != exclude_stage:
            filtered_order_query |= Q(order__Ord_states__name__contains=stage)
    
    return filtered_order_query

# دالة عامة لعرض النتائج المفلترة
def filter_view(request, template_name, machine_names, additional_stages):
    # المرحلة الحالية هي آخر مرحلة في قائمة المراحل
    current_stage = additional_stages[-1]
    # إنشاء فلتر بدون المرحلة الحالية
    filtered_order_query = get_filtered_order_query(additional_stages, current_stage)

    machines = Machine_Order.objects.filter(machine__machine_name__in=machine_names).distinct()
    orders = machines.filter(filtered_order_query).distinct().order_by('-id')
    section = machines.filter(order__Ord_states__name__contains=current_stage).order_by('-id')
    
    context = {
        'machines': machines,
        'orders': orders,
        'section': section,
        'title': machine_names[0],  # إضافة العنوان بناءً على اسم الآلة
        'machine_name': machine_names[0],  # إضافة اسم الماكينة
    }
    
    return render(request, template_name, context)

# تعريف المراحل العامة
base_stages = [
    'تصميم',
    'مونتاج',
    'أفلام',
    'شراء ورق',
    'ورق',
    'شيتر',
    'تجهيز ورق',
    'GTO(1) طباعة ربع',
    'SM(2) طباعة ربع',
    'SM(5) طباعة ربع',
    'SORM طباعة نص',
    'SM(2) طباعة نص',
    'SM طباعة فرخ',
    'CD(5) طباعة فرخ',
    'سلوفان',
    'خدمات طباعة ورنيش/يوفي',
    'خدمات طباعة خارجي',
    'DIE 46 تكسير',
    'DIE 57 تكسير',
    'BOBST تكسير',
    'التسليك و التنظيف',
    'PACTEK 85 تلزيق',
    'PACTEK 65 تلزيق',
    'FG  تلزيق',
    'SBL  تلزيق',
    'تلزيق يدوي',
    'تجليد',
    'قص بضاعة منتهية',
    'تلزيق خارجي'
]


def machine_filter_view(request, machine_name):
    machine_names = [machine_name]
    additional_stages = base_stages[:base_stages.index(machine_name) + 1]
    return filter_view(request, 'machinfilter/otherfilter.html', machine_names, additional_stages)