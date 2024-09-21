from urllib import request
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django_tables2 import SingleTableView
from .table import *
from django_filters.views import FilterView
from .filters import *
#get get_object_or_404
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


from django_tables2 import RequestConfig
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404
#import @login_required
from django.contrib.auth.decorators import login_required

 
@login_required(login_url='login')
def transaction(request):
    in_stock=In_stock.objects.all()
    out_stock=Out_Stock.objects.all()
    in_stock_table = In_StockTable(In_stock.objects.order_by('-date'))
    out_stock_table = Out_StockTable(Out_Stock.objects.order_by('-date'))
    filterin = In_StockFilter(request.GET, queryset=in_stock)
    filterout = Out_StockFilter(request.GET, queryset=out_stock)
    in_stock_table = filterin.qs
    out_stock_table = filterout.qs
    in_stock_table = In_StockTable(in_stock_table)
    out_stock_table = Out_StockTable(out_stock_table)
    RequestConfig(request, paginate={'per_page': 30}).configure(in_stock_table)
    RequestConfig(request, paginate={'per_page': 30}).configure(out_stock_table)
    return render(request, 'storge/main/transaction.html', {'in_stock_table': in_stock_table, 'out_stock_table': out_stock_table, 'filterin': filterin, 'filterout': filterout})

#عرض قايمه بالموردين
@login_required(login_url='login')
def supplier_view(request):
    supplier=Supplier.objects.all()
    table = SupplierTable(supplier)
    filter = SupplierFilter(request.GET, queryset=supplier)
    supplier = filter.qs
    table = SupplierTable(supplier)
    RequestConfig(request, paginate={'per_page': 30}).configure(table)
    context = { 'supplier': supplier,'filter': filter, 'table': table}
    return render(request, 'storge/supplier/supplier.html', context)
    
#اضافه مورد
@login_required(login_url='login')
def supplier_add_view(request):
    form = SupplierForm()
    user = User.objects.first()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.save()

            return redirect('supplier')
    context = {'form': form}
    return render(request, 'storge/supplier/supplier_add.html', context)
    
#تعديل على الموردين  
@login_required(login_url='login')       
def supplier_update_view(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    form = SupplierForm(instance=supplier)
    user=User.objects.first()
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.save()
        
            return redirect('supplier')
    context = {'form': form}
    return render(request, 'storge/supplier/supplier_update.html', context)


@login_required(login_url='login')
def InStockNember_view(request):
    in_stock=InStockNumber.objects.all()
#defolt sort by number
    in_stock = in_stock.order_by('-number')
    table = InStockNumberTable(in_stock)
    filter = InStockNumberFilter(request.GET, queryset=in_stock)
    in_stock = filter.qs
    table = InStockNumberTable(in_stock)
    RequestConfig(request, paginate={'per_page': 30}).configure(table)
    form = InStockNumberForm()
    
    if request.method == 'POST':
        form = InStockNumberForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()

            return redirect('InStockNumber')

    context = { 'in_stock': in_stock,'filter': filter, 'table': table,'form': form}
    return render(request, 'storge/InStock/instocknumber.html', context)

@login_required(login_url='login')
def InStockNember_update_view(request, pk):
    in_stock = get_object_or_404(InStockNumber, pk=pk)
    form = InStockNumberForm2(instance=in_stock)
    #number=InStockNumber.objects.get(id=pk)

    if request.method == 'POST':
        form = InStockNumberForm2(request.POST, instance=in_stock)
        if form.is_valid():
            form = form.save(commit=False)
            #form.number = number
            form.save()
        
            return redirect('InStockNumber')
    context = {'form': form}
    return render(request, 'storge/InStock/instocknumber_update.html', context)

#اضافه صنف جديد 
@login_required(login_url='login')
def iteam_add_view(request):
    form = IteamForm()
    
    if request.method == 'POST':
        form = IteamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iteam')
    else:
        form = IteamForm()

    context = {'form': form}
    return render(request, 'storge/iteam/iteam_add.html', context)     

#صفحه الرئيسيه للصنف
@login_required(login_url='login')
def iteam_view(request):
    iteam=Iteam.objects.all()
    table = IteamTable(iteam)
    filter = IteamFilter(request.GET, queryset=iteam)
    iteam = filter.qs
    table = IteamTable(iteam)
    RequestConfig(request, paginate={'per_page': 30}).configure(table)
    context = { 'iteam': iteam,'filter': filter, 'table': table}
    return render(request, 'storge/iteam/iteam_main.html', context)
 
@login_required(login_url='login')
def in_stock_view(request,pk):
    in_stocknumber = InStockNumber.objects.get(id=pk)
    in_stock=In_stock.objects.filter(in_stocknumber=in_stocknumber)
    table = In_stockTable(in_stock)
    filter = In_stockFilter(request.GET, queryset=in_stock)
    in_stock = filter.qs
    table = In_stockTable(in_stock)
    RequestConfig(request, paginate={'per_page': 30}).configure(table)
    form = In_stockForm()
    if request.method == 'POST':
        form = In_stockForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.in_stocknumber = in_stocknumber
            form.save()

            return redirect('in_stock',pk=in_stocknumber.id)
   

    context = { 'in_stock': in_stock,'filter': filter, 'table': table,'form': form,'in_stocknumber':in_stocknumber}
    return render(request, 'storge/InStock/in_stock.html', context)

@login_required(login_url='login')
#form set 
def in_stock_add_view(request, pk):
    in_stocknumber = get_object_or_404(InStockNumber,pk=pk)
    formset=In_stockFormSet()
    if request.method == 'POST':
        formset=In_stockFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                in_stock=form.save(commit=False)
                in_stock.in_stocknumber=in_stocknumber
                in_stock.save()
            return redirect('in_stock',pk=in_stocknumber.id)
    context = {'formset': formset,'in_stocknumber':in_stocknumber}
    return render(request,'storge/InStock/in_stock_add.html',context)

@login_required(login_url='login')
def in_stock_supplier_view(request,pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    in_stocknumber = InStockNumber.objects.get(supplier=supplier)
    in_stock=In_stock.objects.filter(in_stocknumber=in_stocknumber)
    table = In_stockTable(in_stock)
    filter = In_stockFilter(request.GET, queryset=in_stock)
    in_stock = filter.qs
    table = In_stockTable(in_stock)
    RequestConfig(request, paginate={'per_page': 30}).configure(table)
    context = { 'in_stock': in_stock,'filter': filter, 'table': table}
    return render(request, 'storge/supplier/in_stock_supplier.html', context)

@login_required(login_url='login')   
def out_stock_customer_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    out_StockNumber = Out_StockNumber.objects.filter(customer=customer)
    out_stoke=Out_Stock.objects.filter(out_stocknumber__in=out_StockNumber)
    tables = out_stockTable(out_stoke)
    filter = out_stockFilter(request.GET, queryset=out_stoke)
    out_stoke = filter.qs
    tables = out_stockTable(out_stoke)
    RequestConfig(request, paginate={'per_page': 30}).configure(tables)  
    context = { 'out_stoke': out_stoke,'filter': filter, 'tables': tables}
    return render(request, 'storge/customer/out_stoke_customer.html', context)

@login_required(login_url='login')
def in_stocks_view(request):
    if request.method == 'POST':
        form = In_stockForm(request.POST)
        if form.is_valid():
            in_stock = form.save(commit=False)
            in_stock.save()
            for inner_form in form.inner_form_set:
                if inner_form.is_valid():
                    inner_form.instance.in_stock = in_stock
                    inner_form.save()
            return redirect('in_stock')
    else:
        form = In_stockForm()
        
    context = {'form': form}
    return render(request, 'storge/in_stock/in_stock_add.html', context)

@login_required(login_url='login')
def custmer_view(request):
    custmer=Customer.objects.all()
    table = customerTable(custmer)
    filter = CustomerFilter(request.GET, queryset=custmer)
    custmer = filter.qs
    table = customerTable(custmer)
    RequestConfig(request, paginate={'per_page': 30}).configure(table)
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            custmer = form.save(commit=False)
            custmer.user = request.user
            custmer.save()
            return redirect("custmer")
        else:
            form = CustomerForm()
    context = { 'custmer': custmer,'filter': filter, 'table': table,'form': form}
    return render(request, 'storge/customer/customer.html', context)

@login_required(login_url='login')
def custmer_update_view(request, pk):
    custmer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(instance=custmer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=custmer)
        if form.is_valid():
            
            form.save()
            return redirect("custmer")
    context = {'form': form}
    return render(request, 'storge/customer/customer_edit.html', context)

@login_required(login_url='login')
def Out_StockNumber_view(request):
    out_stocknumber=Out_StockNumber.objects.all() 
    #defolt sort by number
    out_stocknumber = Out_StockNumber.objects.order_by('-number') 
    table = Out_StockNumberTable(out_stocknumber)
    filter = Out_StockNumberFilter(request.GET, queryset=out_stocknumber)
    out_stocknumber = filter.qs
    table = Out_StockNumberTable(out_stocknumber)
    RequestConfig(request, paginate={'per_page': 30}).configure(table)
    form = Out_StockNumberForm()
    if request.method == 'POST':
        form = Out_StockNumberForm(request.POST)
        if form.is_valid():
            out_stocknumber = form.save(commit=False)
            out_stocknumber.user = request.user
            out_stocknumber.save()
            return redirect("OutStockNumber")
        else:
            form = Out_StockNumberForm()
    context = { 'out_stocknumber': out_stocknumber,'filter': filter, 'table': table,'form': form}
    return render(request, 'storge/OutStock/out_stocknumber.html', context)

@login_required(login_url='login')
def Out_StockNumber_update_view(request, pk):
    out_stocknumber = get_object_or_404(Out_StockNumber, pk=pk)
    form = Out_StockNumberForm2(instance=out_stocknumber)
    if request.method == 'POST':
        form = Out_StockNumberForm2(request.POST, instance=out_stocknumber)
        if form.is_valid():
            
            form.save()
            return redirect("OutStockNumber")
    context = {'form': form}
    return render(request, 'storge/OutStock/out_stocknumber_edit.html', context)

@login_required(login_url='login')
def out_stock_view(request, pk): 
    out_stocknumber = get_object_or_404(Out_StockNumber, pk=pk)
    out_stoke= Out_Stock.objects.filter(out_stocknumber=out_stocknumber)

    tables = out_stockTable(out_stoke)
    filter = out_stockFilter(request.GET, queryset=out_stoke)
    out_stoke = filter.qs
    tables = out_stockTable(out_stoke)
    RequestConfig(request, paginate={'per_page': 30}).configure(tables)
    form = Out_stokeForm()
    if request.method == 'POST':
        form = Out_stokeForm(request.POST)
        if form.is_valid():
            out_stoke = form.save(commit=False)
            out_stoke.out_stocknumber = out_stocknumber
            out_stoke.iteam = out_stoke.in_stock.iteam
            out_stoke.save()
            return redirect("out_stock",pk=out_stocknumber.id)
        else:
            form = Out_stokeForm()

    context = { 'out_stoke': out_stoke,'filter': filter, 'tables': tables,'form': form,'out_stocknumber':out_stocknumber}
    return render(request, 'storge/OutStock/out_stock.html', context)
  
@login_required(login_url='login')
def out_stock_add_view(request, pk):
    out_stocknumber = get_object_or_404(Out_StockNumber,pk=pk)
    formset=Out_stokeFormSet()
    if request.method == 'POST':
        formset=Out_stokeFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                out_stoke=form.save(commit=False)
                out_stoke.out_stocknumber=out_stocknumber
                out_stoke.save()
            return redirect('out_stock',pk=out_stocknumber.id)
    context = {'formset': formset,'out_stocknumber':out_stocknumber}
    return render(request, 'storge/OutStock/out_stock_add.html', context)

@login_required(login_url='login')
def out_stock_update_view(request, pk):
    out_stoke = get_object_or_404(Out_Stock, pk=pk)
    form = Out_stokeForm(instance=out_stoke)
    if request.method == 'POST':
        form = Out_stokeForm(request.POST, instance=out_stoke)
        if form.is_valid():
            form.save()
            return redirect("out_stoke")
    context = {'form': form}
    return render(request, 'storge/OutStock/out_stoke_edit.html', context)

@login_required(login_url='login')
def out_stock_all_view(request):
    out_stoke=Out_Stock.objects.all()
    tables = out_stockTable(out_stoke)
    filter = out_stockFilter(request.GET, queryset=out_stoke)
    out_stoke = filter.qs
    tables = out_stockTable(out_stoke)
    RequestConfig(request, paginate={'per_page': 30}).configure(tables)
    form = Out_stoke_allForm()
    if request.method == 'POST':
        form = Out_stoke_allForm(request.POST)
        if form.is_valid():
            out_stoke = form.save(commit=False)
            out_stoke.save()
            return redirect("out_stoke_all")
        else:
            form = Out_stoke_allForm()


    context = { 'out_stoke': out_stoke,'filter': filter, 'tables': tables,'form': form}
    return render(request, 'storge/OutStock/out_stoke_all.html', context)

@login_required(login_url='login')
def item_stock_veiw (request):
    
    table = StockTable(Iteam.objects.all())
    filter = IteamFilter(request.GET, queryset=Iteam.objects.all())
    table = filter.qs
    table = StockTable(table)
    RequestConfig(request, paginate={'per_page': 30}).configure(table)
    context = {'table': table, 'filter': filter}
 
    return render(request, 'storge/main/item_stock.html', context)














