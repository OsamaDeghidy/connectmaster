from asyncore import close_all
from pstats import Stats
from re import X
from unicodedata import name
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from Work_Orders.models import Customer, Product,CorrectiveActions,Design_And_Printing_Specifications,Paper_Specification,Aftar_Print_Services,Crushing_Data,Gluing_And_Binding_Data,Finished_product_and_packing_data
from .models import Order,Paper_and_cardboard_data,Order_states,OrderDeliveryDate
from .forms import NewOrderForm,New_Paper_and_cardboard_data_Form,OrderDeliveryDateForm, RDDForm, EDDForm
from Work_Orders.forms import CorrectiveActionsForm
from django.db.models import Q
# Create your views here.



def OrderDeliveryDateveiw_list(request):    
    
    orders = Order.objects.filter(~Q(Ord_states__name__in=['Closed', 'حسابات', 'Invoiced','Deleted'])).order_by('-id')
    return render(request, 'ODD/ODD_list.html', {'orders': orders})


@login_required
def edit_order_delivery_date(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_delivery_date_instance = order.Ord_delivery_date
    
    if request.method == 'POST':
        form = OrderDeliveryDateForm(request.POST, instance=order_delivery_date_instance)
        if form.is_valid():
            order_delivery_date_instance = form.save(commit=False)
            order_delivery_date_instance.save()
            order.Ord_delivery_date = order_delivery_date_instance
            order.save()
           
    else:
        form = OrderDeliveryDateForm(instance=order_delivery_date_instance)
    
    return render(request, 'ODD/edit_order_delivery_date.html', {'form': form, 'order_id': order_id,'orders':order})




@login_required
def edit_rdd(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    # Check if delivery date exists, if not create a new instance
    if order.Ord_delivery_date:
        rdd_instance = order.Ord_delivery_date
    else:
        rdd_instance = OrderDeliveryDate()  # Assuming `OrderDeliveryDate` is the model for `Ord_delivery_date`

    if request.method == 'POST':
        form = RDDForm(request.POST, instance=rdd_instance)
        if form.is_valid():
            rdd_instance = form.save(commit=False)
            rdd_instance.save()
            order.Ord_delivery_date = rdd_instance
            order.save()  # Ensure the order is updated with the new delivery date
            return JsonResponse({'success': True, 'close_modal': True})  # Return success response for AJAX
    else:
        form = RDDForm(instance=rdd_instance)
    
    return render(request, 'ODD/edit_rdd.html', {'form': form, 'order_id': order_id, 'orders': order})

@login_required
def edit_edd(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    # Check if delivery date exists, if not create a new instance
    if order.Ord_delivery_date:
        edd_instance = order.Ord_delivery_date
    else:
        edd_instance = OrderDeliveryDate()  # Assuming `OrderDeliveryDate` is the model for `Ord_delivery_date`

    if request.method == 'POST':
        form = EDDForm(request.POST, instance=edd_instance)
        if form.is_valid():
            edd_instance = form.save(commit=False)
            edd_instance.save()
            order.Ord_delivery_date = edd_instance
            order.save()  # Ensure the order is updated with the new delivery date
            return JsonResponse({'success': True, 'close_modal': True})  # Return success response for AJAX
    else:
        form = EDDForm(instance=edd_instance)
    
    return render(request, 'ODD/edit_edd.html', {'form': form, 'order_id': order_id, 'orders': order})

@login_required
def product_orders(request,Sector_id, Customer_id, Product_id):
     product = get_object_or_404(Product,  Product_Sector__pk= Sector_id, Product_Customer__pk= Customer_id, pk = Product_id )
    
     orders = Order.objects.filter(Ord_Product__pk = Product_id)

     corrective_actions = CorrectiveActions.objects.filter(product__pk = Product_id)
    
    
    
     return render (request,'orders/Product_Orders.html',{'product':product ,'orders':orders,'corrective_actions':corrective_actions})
@login_required
def new_corrective_action(request, product_id):
    if request.method == 'POST':
        form = CorrectiveActionsForm(request.POST)
        if form.is_valid():
            corrective_action = form.save(commit=False)
            corrective_action.product_id = product_id
            corrective_action.save()
            return redirect('product_orders', Sector_id=corrective_action.product.Product_Sector.pk, Customer_id=corrective_action.product.Product_Customer.pk, Product_id=product_id)
    else:
        form = CorrectiveActionsForm()
    return render(request, 'corrective_action/new_corrective_action.html', {'form': form})



def edit_corrective_action(request, corrective_action_id):
    # Get the corrective action object
    corrective_action = get_object_or_404(CorrectiveActions, pk=corrective_action_id)
    
    if request.method == 'POST':
        # If the request method is POST, initialize the form with the POST data and the instance of corrective action
        form = CorrectiveActionsForm(request.POST, instance=corrective_action)
        if form.is_valid():
            # Save the updated corrective action
            form.save()
            #return redirect('product_orders', Sector_id=corrective_action.product.Product_Sector.pk, Customer_id=corrective_action.product.Product_Customer.pk, Product_id=corrective_action.product.pk)
            

    else:
        # If it's a GET request, initialize the form with the instance of corrective action
        form = CorrectiveActionsForm(instance=corrective_action)
    
    # Render the template with the form
    return render(request, 'corrective_action/edit_corrective_action.html', {'form': form})

@login_required
def new_order(request,Sector_id,Customer_id,Product_id):
     customer = get_object_or_404(Customer, pk = Customer_id)
     product = get_object_or_404(Product, Product_Sector__pk = Sector_id, Product_Customer__pk = Customer_id, pk= Product_id)
     form = NewOrderForm()
     form_2 = New_Paper_and_cardboard_data_Form()
     user = User.objects.get(username=request.user)
     if request.method == "POST":
          form = NewOrderForm(request.POST)
          form_2 = New_Paper_and_cardboard_data_Form(request.POST)
          if all ([form.is_valid(),form_2.is_valid()]):
               Order = form.save(commit=False)
               Paper_and_cardboard_data= form_2.save(commit=False)
               Order.Ord_Product = product
               Order.Ord_Created_By = user
               Order.Ord_Customer_Name = customer
               Order.save()
               Paper_and_cardboard_data.CARD_Order = Order
               Paper_and_cardboard_data.save()
               #return redirect('orders:product_orders', Sector_id= Sector_id, Customer_id= Customer_id, Product_id= Product_id)
               return redirect ('product_orders',Product_id=product.pk, Customer_id=product.Product_Customer.pk, Sector_id=product.Product_Sector.pk)
     else:
          form=NewOrderForm
     
     return render (request,'orders/New_Order.html',{'product':product,'form':form,'form_2':form_2})


@login_required
def OrderUpdatedView (request,Sector_id,Customer_id,Product_id,Order_id):
     product = get_object_or_404(Product, Product_Sector__pk = Sector_id, Product_Customer__pk = Customer_id, pk= Product_id)
     orders = get_object_or_404(Order, pk = Order_id)
     paper_and_cardboard_data = get_object_or_404(Paper_and_cardboard_data, CARD_Order__pk = Order_id)
     form = NewOrderForm(instance=orders)
     form_2 = New_Paper_and_cardboard_data_Form(instance=paper_and_cardboard_data)
     useredite = User.objects.get(username=request.user)
     code = orders.Ord_work_order_number
     orders.Ord_code_Edited = code

     if request.method == "POST":
          form = NewOrderForm(request.POST,instance=orders)
          form_2 = New_Paper_and_cardboard_data_Form(request.POST,instance=paper_and_cardboard_data)
          if all ([form.is_valid(),form_2.is_valid()]):
               orders = form.save(commit=False)
               paper_and_cardboard_data= form_2.save(commit=False)
               orders.Ord_updated_by = useredite
               orders.Ord_work_order_number=orders.Ord_code_Edited
               orders.save()
               paper_and_cardboard_data.save()
               form.save()
               form_2.save()
               return redirect ('Order_details',Order_id=Order_id)
     else:
          form=NewOrderForm(instance=orders)
          form_2=New_Paper_and_cardboard_data_Form(instance=paper_and_cardboard_data)
     return render (request,'orders/OrderUpdatedView.html',{'orders':orders,'form':form,'form_2':form_2,'product':product})
     


@login_required
def OrderStatusupdate(request,Sector_id,Customer_id,Product_id,Order_id):
     orders = get_object_or_404(Order, pk = Order_id)
     form = NewOrderForm(instance=orders.Ord_states)
     useredite = User.objects.get(username=request.user)
     code = orders.Ord_work_order_number
     orders.Ord_code_Edited = code

     if request.method == "POST":
          form = NewOrderForm(request.POST,instance=orders)
       
          if form.is_valid():
               orders = form.save(commit=False)
               orders.Ord_updated_by = useredite
               orders.save()
               form.save()
               
               return JsonResponse({'success': True})  # Return success response for AJAX request               
     else:
          form=NewOrderForm(instance=orders)
     return render (request,'orders/OrderStatusupdate.html',{'orders':orders,'form':form})


@login_required
def print_order (request,Order_id):
     orders = get_object_or_404(Order, pk = Order_id)
     paper_and_cardboard_data = get_object_or_404(Paper_and_cardboard_data, CARD_Order__pk = Order_id)
     return render (request,'orders/print_order.html',{'orders':orders,'paper_and_cardboard_data':paper_and_cardboard_data})         

               
#.order_by('-Ord_Created_Dt')
@login_required
def Prepressied (request):
     New = Order.objects.filter(Ord_states__name__contains='جديد').order_by('-id')
     design = Order.objects.filter(Ord_states__name__contains = 'تصميم').order_by('-id')
     Produced_by = Order.objects.filter(Ord_states__name__contains = 'مونتاج').order_by('-id')
     aflam = Order.objects.filter(Ord_states__name__contains = 'أفلام').order_by('-id')
  
     
    
     Stats = Order_states.objects.all () 
     
     return render (request,'orders/Prepressied.html',{'Stats':Stats,'New':New,'design':design,'Produced_by':Produced_by,'aflam':aflam,})

@login_required
def paperpreprat_veiw (request):
     aflam = Order.objects.filter(Ord_states__name__contains = 'أفلام').order_by('-id')
     buy_paper = Order.objects.filter(Ord_states__name__contains = 'شراء ورق').order_by('-id')
     paper = Order.objects.filter(Ord_states__name__contains='ورق').exclude(Ord_states__name__contains='تجهيز ورق').exclude(Ord_states__name__contains='شراء ورق').order_by('-id')
     chitter = Order.objects.filter(Ord_states__name__contains = 'شيتر').order_by('-id')
     paper_processing = Order.objects.filter(Ord_states__name__contains = 'تجهيز ورق').order_by('-id')
     
    
     Stats = Order_states.objects.all () 
     
     return render (request,'orders/paperpreprat.html',{'aflam':aflam,'Stats':Stats,'buy_paper':buy_paper,'paper':paper,'chitter':chitter,'paper_processing':paper_processing})
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required
def In_progress (request):  #PRINTING 
     paper_processing = Order.objects.filter(Ord_states__name__contains = 'تجهيز ورق').order_by('-id')
     #-------طباعه------------------------------------------------------------------------
     Gto= Order.objects.filter(Ord_states__name__contains = 'GTO(1) طباعة ربع').order_by('-id')
     SM = Order.objects.filter(Ord_states__name__contains = 'SM(2) طباعة ربع').order_by('-id')
     SM5 = Order.objects.filter(Ord_states__name__contains = 'SM(5) طباعة ربع').order_by('-id')#add

     SORM = Order.objects.filter(Ord_states__name__contains = 'SORM طباعة نص').order_by('-id')
     SM2 = Order.objects.filter(Ord_states__name__contains = 'SM(2) طباعة نص').order_by('-id')#add

     SM_chick = Order.objects.filter(Ord_states__name = 'SM طباعة فرخ').order_by('-id')
     SD_SM = Order.objects.filter(Ord_states__name__contains = 'CD(5) طباعة فرخ').order_by('-id')


    
     
     return render (request,'orders/In_progress.html',{'paper_processing':paper_processing,'Gto':Gto,'SM':SM,'SM5':SM5,'SORM':SORM,'SM2':SM2 ,'SM_chick':SM_chick,'SD_SM':SD_SM,})
 
@login_required
def PrintingServics_veiw  (request):  #PRINTING 

     cellophane = Order.objects.filter(Ord_states__name__contains = 'سلوفان').order_by('-id')
     #------- ----خدمات طباعه -------------------------------------------------------------------------
     Varnish_UV = Order.objects.filter(Ord_states__name__contains = 'خدمات طباعة ورنيش/يوفي').order_by('-id')
     Outside_printing = Order.objects.filter(Ord_states__name__contains = 'خدمات طباعة خارجي').order_by('-id')
     #-----------------------تكسير-----------------------------------------------------------------------------



    
     
     return render (request,'orders/PrintingServics.html',{'cellophane':cellophane,'Varnish_UV':Varnish_UV,'Outside_printing':Outside_printing,})

@login_required
def diecvting_veiw (request):  #PRINTING 

   
     #-----------------------تكسير-----------------------------------------------------------------------------
     DIE_46 = Order.objects.filter(Ord_states__name__contains = 'DIE 46 تكسير').order_by('-id')
     DIE_57 = Order.objects.filter(Ord_states__name__contains = 'DIE 57 تكسير').order_by('-id')
     BOBST = Order.objects.filter(Ord_states__name__contains = 'BOBST تكسير').order_by('-id')
     #-------------------------------------------------------------------------------------------------
     cleaning = Order.objects.filter(Ord_states__name__contains = 'التسليك و التنظيف').order_by('-id')
  


    
     
     return render (request,'orders/diecvting.html',{'DIE_46':DIE_46,'DIE_57':DIE_57,'BOBST':BOBST,'cleaning':cleaning,})


@login_required
def gluing_veiw (request):  #PRINTING 


     #-----------------------تلزيق------------------------------------------------------------------------
     BACTED_8S = Order.objects.filter(Ord_states__name__contains = 'PACTEK 85 تلزيق').order_by('-id')
     BACTECHGS = Order.objects.filter(Ord_states__name__contains = 'PACTEK 65 تلزيق').order_by('-id')
     FG = Order.objects.filter(Ord_states__name__contains = 'FG  تلزيق').order_by('-id')
     SBL= Order.objects.filter(Ord_states__name__contains = 'SBL  تلزيق').order_by('-id')
     Manual = Order.objects.filter(Ord_states__name__contains = 'تلزيق يدوي').order_by('-id')
     #-------------------------------------------------------------------------------------------------
     bind = Order.objects.filter(Ord_states__name__contains = 'تجليد').order_by('-id')
     finished_goods = Order.objects.filter(Ord_states__name__contains = 'قص بضاعة منتهية').order_by('-id')
     external_adhesive = Order.objects.filter(Ord_states__name__contains = 'تلزيق خارجي').order_by('-id')


    
     
     return render (request,'orders/gluing.html',{'BACTED_8S':BACTED_8S,'BACTECHGS':BACTECHGS,'FG':FG,'SBL':SBL,'Manual':Manual,'bind':bind,'finished_goods':finished_goods,'external_adhesive':external_adhesive})
  
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def opend_orders(request):
     New = Order.objects.filter(Ord_states__name__contains='جديد').order_by('-id')
     design = Order.objects.filter(Ord_states__name__contains = 'تصميم').order_by('-id')
     Produced_by = Order.objects.filter(Ord_states__name__contains = 'مونتاج').order_by('-id')
     aflam = Order.objects.filter(Ord_states__name__contains = 'أفلام').order_by('-id')

     buy_paper = Order.objects.filter(Ord_states__name__contains = 'شراء ورق').order_by('-id')
     paper = Order.objects.filter(Ord_states__name__contains='ورق').exclude(Ord_states__name__contains='تجهيز ورق').exclude(Ord_states__name__contains='شراء ورق').order_by('-id')
     chitter = Order.objects.filter(Ord_states__name__contains = 'شيتر').order_by('-id')
     paper_processing = Order.objects.filter(Ord_states__name__contains = 'تجهيز ورق').order_by('-id')
     paper_processing = Order.objects.filter(Ord_states__name__contains = 'تجهيز ورق').order_by('-id')

     Gto= Order.objects.filter(Ord_states__name__contains = 'GTO(1) طباعة ربع').order_by('-id')
     SM = Order.objects.filter(Ord_states__name__contains = 'SM(2) طباعة ربع').order_by('-id')
     SM5 = Order.objects.filter(Ord_states__name__contains = 'SM(5) طباعة ربع').order_by('-id')

     SORM = Order.objects.filter(Ord_states__name__contains = 'SORM طباعة نص').order_by('-id')
     SM2 = Order.objects.filter(Ord_states__name__contains = 'SM(2) طباعة نص').order_by('-id')

     SM_chick = Order.objects.filter(Ord_states__name = 'SM طباعة فرخ').order_by('-id')
     SD_SM = Order.objects.filter(Ord_states__name__contains = 'CD(5) طباعة فرخ').order_by('-id')
     
     slofan = Order.objects.filter(Ord_states__name__contains = 'سلوفان').order_by('-id') 
     uv = Order.objects.filter(Ord_states__name__contains = 'خدمات طباعة ورنيش/يوفي').order_by('-id')
     outside_printing = Order.objects.filter(Ord_states__name__contains = 'خدمات طباعة خارجي').order_by('-id')



     DIE_46 = Order.objects.filter(Ord_states__name__contains = 'DIE 46 تكسير').order_by('-id')
     DIE_57 = Order.objects.filter(Ord_states__name__contains = 'DIE 57 تكسير').order_by('-id')
     BOBST = Order.objects.filter(Ord_states__name__contains = 'BOBST تكسير').order_by('-id')

     cleaning = Order.objects.filter(Ord_states__name__contains = 'التسليك و التنظيف').order_by('-id')
     BACTED_8S = Order.objects.filter(Ord_states__name__contains = 'PACTEK 85 تلزيق').order_by('-id')
     BACTECHGS = Order.objects.filter(Ord_states__name__contains = 'PACTEK 65 تلزيق').order_by('-id')
     FG = Order.objects.filter(Ord_states__name__contains = 'FG  تلزيق').order_by('-id')
     SBL= Order.objects.filter(Ord_states__name__contains = 'SBL  تلزيق').order_by('-id')
     Manual = Order.objects.filter(Ord_states__name__contains = 'تلزيق يدوي').order_by('-id')

     bind = Order.objects.filter(Ord_states__name__contains = 'تجليد').order_by('-id')
     finished_goods = Order.objects.filter(Ord_states__name__contains = 'قص بضاعة منتهية').order_by('-id')
     external_adhesive = Order.objects.filter(Ord_states__name__contains = 'تلزيق خارجي').order_by('-id')
     

     return render (request,'order_filter/opend_orders.html',{'New':New,'design':design,'Produced_by':Produced_by,'aflam':aflam,'buy_paper':buy_paper,'paper':paper,'chitter':chitter,'paper_processing':paper_processing,'Gto':Gto,'SM':SM,'SM5':SM5,'SORM':SORM,'SM2':SM2,'SM_chick':SM_chick,'SD_SM':SD_SM,'slofan':slofan,'uv':uv,'outside_printing':outside_printing,'DIE_46':DIE_46,'DIE_57':DIE_57,'BOBST':BOBST,'cleaning':cleaning,'BACTED_8S':BACTED_8S,'BACTECHGS':BACTECHGS,'FG':FG,'SBL':SBL,'Manual':Manual,'bind':bind,'finished_goods':finished_goods,'external_adhesive':external_adhesive})

#VEIW to filter order states  ('Under Delivery', 'Under Delivery'),#NEW STATES 
@login_required
def Under_Delivery(request):
     orders = Order.objects.filter(Ord_states__name__contains = 'Under Delivery').order_by('-id')
     return render (request,'ODD/ODD_list.html',{'orders':orders})


@login_required
def Closed (request):
     orders = Order.objects.filter(Ord_states__name__contains = 'Finished').order_by('-id')
     return render (request,'orders/Closed.html',{'Stats':Stats,'orders':orders})
@login_required
def Fenished (request):
     orders = Order.objects.filter(Ord_states__name__contains = 'حسابات').order_by('-id')
     return render (request,'orders/Fenished.html',{'Stats':Stats,'orders':orders})
@login_required     
def In_voiced (request):
     orders = Order.objects.filter(Ord_states__name__contains = 'Closed').order_by('-id')     
     return render (request,'orders/In_voiced.html',{'Stats':Stats,'orders':orders})
@login_required
def Deleted (request):
     orders = Order.objects.filter(Ord_states__name__contains = 'Deleted').order_by('-id')  
     return render (request,'orders/Deleted.html',{'Stats':Stats,'orders':orders}) 

@login_required
def Order_details (request,Order_id):
     orders = get_object_or_404(Order, pk = Order_id)
     paper_and_cardboard_data = get_object_or_404(Paper_and_cardboard_data, CARD_Order__pk = Order_id)

     return render (request,'orders/Order_details.html',{'orders':orders,'paper_and_cardboard_data':paper_and_cardboard_data})      



# veiw to filter order as Order.Ord_Product.customer_representative



@login_required
def filter_orders_by_representative(request, representative_name):
    filtered_orders = Order.objects.filter(Ord_Product__customer_representative=representative_name)
    return render(request, 'ODD/ODD_list.html', {'orders': filtered_orders, 'representative_name': representative_name})
