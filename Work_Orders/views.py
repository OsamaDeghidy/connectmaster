from datetime import timezone
from re import X
from tkinter.tix import Form
from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.http import HttpResponseRedirect
from numpy import count_nonzero
from requests import request
from django.db.models import Q
from Order.models import OrderDeliveryDate
from .models import Account, Aftar_Print_Services, Crushing_Data, Customer, Finished_product_and_packing_data, Gluing_And_Binding_Data, Order, Paper_Specification, Product, Sector,Design_And_Printing_Specifications
from django.contrib.auth.models import User
from .forms import NewCustomerALLForm, NewCustomerForm
from .forms import NewProductForm
from .forms import NewOrderForm, Design_And_Printing_SpecificationsForm,Paper_SpecificationForm
from .forms import Aftar_Print_ServicesForm,Crushing_DataForm,Gluing_And_Binding_DataForm,Finished_product_and_packing_dataForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count


def not_in_marketing_group(user):
    return not user.groups.filter(name='markting').exists()

def forbidden_page(request):
    return render(request, 'user auth/forbidden_page.html')

@login_required
def sectors(request):
    sectors = Sector.objects.all()
    return render (request,'Sectors.html',{'sectors':sectors})


@user_passes_test(not_in_marketing_group, login_url='forbidden_page')
def customers(request):
    customers = Customer.objects.all()
    return render(request, 'Customers.html', {'customers': customers})
@login_required
def orders(request):
    orders = Order.objects.all()
    
    return render (request,'Orders.html',{'orders':orders})

@login_required
def sector_customers(request,Sector_id):
     sector = get_object_or_404(Sector,pk=Sector_id)
     return render (request,'Sector_Customers.html',{'sector':sector})

@login_required
def customer_products(request,Sector_id,Customer_id):
     customer = get_object_or_404(Customer, Customer_Sector__pk = Sector_id, pk = Customer_id)
     return render (request,'Customer_Products.html',{'customer':customer})
@login_required     
def customer_print(request,Sector_id,Customer_id):
     customer = get_object_or_404(Customer, Customer_Sector__pk = Sector_id, pk = Customer_id)
     return render (request,'customer_print.html',{'customer':customer})



def new_customer_all(request):  # Create a new customer
          form = NewCustomerALLForm()  # Create a new form
          user = User.objects.get(username=request.user)   # Get the first user
          # if sector_id is not None:
          
          if request.method == "POST": # If the form has been submitted
               form = NewCustomerALLForm(request.POST) # Get the data from the submitted form
               if form.is_valid():      # If the form is valid
                    Customer = form.save(commit=False) # Save the form data
                    Customer.Created_By = user # Set the user
                    Customer.Customer_Sector=Sector.objects.get(pk=request.POST['Customer_Sector'])

                    #Customer.Created_By = request.POST.get('Created_By')
                    Customer.save() # Save the data
                    return redirect ('customers')
          else:
               form=NewCustomerALLForm
          return render (request,'new_customer_all.html',{'form':form})
          




@login_required
def new_customer(request,Sector_id):
     sector = get_object_or_404(Sector,pk=Sector_id)
     form = NewCustomerForm()
     user = User.objects.first()
     if request.method == "POST":
          form = NewCustomerForm(request.POST)
          if form.is_valid():
               Customer = form.save(commit=False)
               Customer.Customer_Sector = sector
               Customer.Created_By = request.user
               Customer.save()
               return redirect ('sector_customers', Sector_id=sector.pk)
     else:
          form=NewCustomerForm
     return render (request,'New_Customer.html', {'sector':sector,'form':form})

def CustomerUpdatedView (request,Sector_id,Customer_id):
     customer = get_object_or_404(Customer, Customer_Sector__pk = Sector_id, pk = Customer_id)
     form = NewCustomerForm(request.POST  or None,instance=customer)
     user = User.objects.first()
     code=customer.customer_code
     customer.Customer_code_edite=code


     if request.method == "POST":
          form = NewCustomerForm(request.POST  or None, instance=customer)
          if form.is_valid():
               customer = form.save(commit=False)
               customer.Created_By = user
               customer.save()
               return redirect ('customers')
    
     return render (request,'customer_update.html',{'form':form}) 



@login_required
def new_product(request, Sector_id, Customer_id):
    customer = get_object_or_404(Customer, Customer_Sector__pk=Sector_id, pk=Customer_id)
    sector = get_object_or_404(Sector, pk=Sector_id)
    
    
    if request.method == "POST":
        form = NewProductForm(request.POST,request.FILES)
        form_2 = Design_And_Printing_SpecificationsForm(request.POST,request.FILES )
        form_3 = Paper_SpecificationForm(request.POST)
        form_4 = Aftar_Print_ServicesForm(request.POST)
        form_5 = Crushing_DataForm(request.POST)
        form_6 = Gluing_And_Binding_DataForm(request.POST)
        form_7 = Finished_product_and_packing_dataForm(request.POST)
        
        if all([form.is_valid(), form_2.is_valid(), form_3.is_valid(), form_4.is_valid(), form_5.is_valid(), form_6.is_valid(), form_7.is_valid()]):
            product = form.save(commit=False)
            product.Product_Customer = customer
            product.Product_Sector = sector
            product.Created_By = request.user
            
            # Check if it's the first time and create data accordingly
            if not product.id:
                product.Product_Design_and_printing_specifications = form_2.save()
                product.Product_paper_specification = form_3.save()
                product.Product_Aftar_Print_Services = form_4.save()
                product.Product_Crushing_Data = form_5.save()
                product.Product_Gluing_And_Binding_Data = form_6.save()
                product.Product_Finished_product_and_packing_data = form_7.save()
            else:
                product.Product_Design_and_printing_specifications = form_2.save() if product.Product_Design_and_printing_specifications else Design_And_Printing_Specifications.objects.create()
                product.Product_paper_specification = form_3.save() if product.Product_paper_specification else Paper_Specification.objects.create()
                product.Product_Aftar_Print_Services = form_4.save() if product.Product_Aftar_Print_Services else Aftar_Print_Services.objects.create()
                product.Product_Crushing_Data = form_5.save() if product.Product_Crushing_Data else Crushing_Data.objects.create()
                product.Product_Gluing_And_Binding_Data = form_6.save() if product.Product_Gluing_And_Binding_Data else Gluing_And_Binding_Data.objects.create()
                product.Product_Finished_product_and_packing_data = form_7.save() if product.Product_Finished_product_and_packing_data else Finished_product_and_packing_data.objects.create()
            
            product.save()
            return redirect('representative_view', customer_id=customer.pk, )
    else:
        form = NewProductForm()
        form_2 = Design_And_Printing_SpecificationsForm()
        form_3 = Paper_SpecificationForm()
        form_4 = Aftar_Print_ServicesForm()
        form_5 = Crushing_DataForm()
        form_6 = Gluing_And_Binding_DataForm()
        form_7 = Finished_product_and_packing_dataForm()
     
    return render(request, 'New_Product.html', {
        'customer': customer,
        'form': form,
        'form_2': form_2,
        'form_3': form_3,
        'form_4': form_4,
        'form_5': form_5,
        'form_6': form_6,
        'form_7': form_7,
    })

from .models import Customer, Sector
@login_required
def edit_product(request, sector_id, customer_id, product_id):
    customer = get_object_or_404(Customer, Customer_Sector__pk=sector_id, pk=customer_id)
    sector = get_object_or_404(Sector, pk=sector_id)
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = NewProductForm(request.POST,request.FILES or None, instance=product)
        form_2 = Design_And_Printing_SpecificationsForm(request.POST,request.FILES or None, instance=product.Product_Design_and_printing_specifications)
        form_3 = Paper_SpecificationForm(request.POST, instance=product.Product_paper_specification)
        form_4 = Aftar_Print_ServicesForm(request.POST, instance=product.Product_Aftar_Print_Services)
        form_5 = Crushing_DataForm(request.POST, instance=product.Product_Crushing_Data)
        form_6 = Gluing_And_Binding_DataForm(request.POST, instance=product.Product_Gluing_And_Binding_Data)
        form_7 = Finished_product_and_packing_dataForm(request.POST, instance=product.Product_Finished_product_and_packing_data)

        if all([form.is_valid(), form_2.is_valid(), form_3.is_valid(), form_4.is_valid(), form_5.is_valid(), form_6.is_valid(), form_7.is_valid()]):
            product = form.save(commit=False)
            product.Product_Customer = customer
            product.Product_Sector = sector
            product.Created_By = request.user

           
            # Check and create related instances if they don't exist
            if not product.Product_Design_and_printing_specifications:
                product.Product_Design_and_printing_specifications = Design_And_Printing_Specifications.objects.create()

            if not product.Product_paper_specification:
                product.Product_paper_specification = Paper_Specification.objects.create()


            if not product.Product_Aftar_Print_Services:
                product.Product_Aftar_Print_Services = Aftar_Print_Services.objects.create()

            if not product.Product_Crushing_Data:
                product.Product_Crushing_Data = Crushing_Data.objects.create()

            if not product.Product_Gluing_And_Binding_Data:
                product.Product_Gluing_And_Binding_Data = Gluing_And_Binding_Data.objects.create()

            if not product.Product_Finished_product_and_packing_data:
                product.Product_Finished_product_and_packing_data = Finished_product_and_packing_data.objects.create()
           

                

            if product.Product_Design_and_printing_specifications:
                form_2.instance = product.Product_Design_and_printing_specifications
                form_2.save()


            if product.Product_paper_specification:
                form_3.instance = product.Product_paper_specification
                form_3.save()

            if product.Product_Aftar_Print_Services:
                form_4.instance = product.Product_Aftar_Print_Services
                form_4.save()

            if product.Product_Crushing_Data:
                form_5.instance = product.Product_Crushing_Data
                form_5.save()

            if product.Product_Gluing_And_Binding_Data:
                form_6.instance = product.Product_Gluing_And_Binding_Data
                form_6.save()

            if product.Product_Finished_product_and_packing_data:
                form_7.instance = product.Product_Finished_product_and_packing_data
                form_7.save()


            product.save()
            

        return redirect('product_orders', Sector_id=sector_id, Customer_id=customer_id, Product_id=product_id)
    else:
        form = NewProductForm(instance=product)
        form_2 = Design_And_Printing_SpecificationsForm(instance=product.Product_Design_and_printing_specifications)
        form_3 = Paper_SpecificationForm(instance=product.Product_paper_specification)
        form_4 = Aftar_Print_ServicesForm(instance=product.Product_Aftar_Print_Services)
        form_5 = Crushing_DataForm(instance=product.Product_Crushing_Data)
        form_6 = Gluing_And_Binding_DataForm(instance=product.Product_Gluing_And_Binding_Data)
        form_7 = Finished_product_and_packing_dataForm(instance=product.Product_Finished_product_and_packing_data)

    return render(request, 'product/Edite.html', {
        'customer': customer,
        'form': form,
        'form_2': form_2,
        'form_3': form_3,
        'form_4': form_4,
        'form_5': form_5,
        'form_6': form_6,
        'form_7': form_7,
    })




@login_required
def print_product(request,Sector_id, Customer_id, Product_id):
     product = get_object_or_404(Product, Product_Sector__pk = Sector_id, Product_Customer__pk = Customer_id, pk = Product_id)
  
     return render (request,'print_product.html',{'product':product })






def all_products_view(request):
     products = Product.objects.all()
     return render (request,'all_products.html',{'products':products})
     


@login_required
def dashboard(request):
     sec=Sector.objects.all().count()
     customers= Customer.objects.all().count()
     products= Product.objects.all().count()
     orders= Order.objects.all().count()
     New = Order.objects.filter(Ord_states__name__contains='جديد').count()
     design = Order.objects.filter(Ord_states__name__contains = 'تصميم').count()
     Produced_by = Order.objects.filter(Ord_states__name__contains = 'مونتاج').count()
     buy_paper = Order.objects.filter(Ord_states__name__contains = 'شراءورق').count()
     paper = Order.objects.filter(Ord_states__name__contains = 'ورق').exclude(Ord_states__name__contains='تجهيز ورق').exclude(Ord_states__name__contains='شراء ورق').count()
     chitter = Order.objects.filter(Ord_states__name__contains = 'شيتر').count()
     paper_processing = Order.objects.filter(Ord_states__name__contains = 'تجهيز ورق').count()
     #-------طباعه------------------------------------------------------------------------
     Gto= Order.objects.filter(Ord_states__name__contains = 'GTO طباعة ربع').count()
     SM = Order.objects.filter(Ord_states__name__contains = 'SM طباعة ربع').count()
     SORM = Order.objects.filter(Ord_states__name__contains = 'SORM طباعة نص').count()
     SM_chick = Order.objects.filter(Ord_states__name = 'SM طباعة فرخ').count()
     SD_SM = Order.objects.filter(Ord_states__name__contains = 'CD-SM طباعة فرخ').count()
     #------------------------------------------------------------------------------
     cellophane = Order.objects.filter(Ord_states__name__contains = 'سلوفان').count()
     #------- ----خدمات طباعه -------------------------------------------------------------------------
     Varnish_UV = Order.objects.filter(Ord_states__name__contains = 'خدمات طباعة ورنيش/يوفي').count()
     Outside_printing = Order.objects.filter(Ord_states__name__contains = 'خدمات طباعة خارجي').count()
     #-----------------------تكسير-----------------------------------------------------------------------------
     DIE_46 = Order.objects.filter(Ord_states__name__contains = 'DIE 46 تكسير').count()
     DIE_57 = Order.objects.filter(Ord_states__name__contains = 'DIE 57 تكسير').count()
     BOBST = Order.objects.filter(Ord_states__name__contains = 'BOBST تكسير').count()
     #-------------------------------------------------------------------------------------------------
     cleaning = Order.objects.filter(Ord_states__name__contains = 'التسليك و التنظيف').count()
     #-----------------------تلزيق------------------------------------------------------------------------
     BACTED_8S = Order.objects.filter(Ord_states__name__contains = 'PACTEK 85 تلزيق').count()
     BACTECHGS = Order.objects.filter(Ord_states__name__contains = 'PACTEK 65 تلزيق').count()
     FG = Order.objects.filter(Ord_states__name__contains = 'FG  تلزيق').count()
     SBL= Order.objects.filter(Ord_states__name__contains = 'SBL  تلزيق').count()
     Manual = Order.objects.filter(Ord_states__name__contains = 'تلزيق يدوي').count()
     #-------------------------------------------------------------------------------------------------
     bind = Order.objects.filter(Ord_states__name__contains = 'تجليد').count()
     finished_goods = Order.objects.filter(Ord_states__name__contains = 'قص بضاعة منتهية').count()
     external_adhesive = Order.objects.filter(Ord_states__name__contains = 'تلزيق خارجي').count()
     Closed = Order.objects.filter(Ord_states__name__contains = 'Closed').count()
     #-------------------------------------------------------------------------------------------------
     Account = Order.objects.filter(Ord_states__name__contains = 'حسابات').count() 
     #-------------------------------------------------------------------------------------------------
     Invoiced = Order.objects.filter(Ord_states__name__contains = 'Invoiced').count()   
     Deleted = Order.objects.filter(Ord_states__name__contains = 'Deleted').count()  
  
     return render (request,'dashboard.html',{'sec':sec,'customers':customers,'products':products,'orders':orders,'New':New,'design':design,'Produced_by':Produced_by,'buy_paper':buy_paper,'paper':paper,'chitter':chitter,'paper_processing':paper_processing,'Gto':Gto,'SM':SM,'SORM':SORM,'SM_chick':SM_chick,'SD_SM':SD_SM,'cellophane':cellophane,'Varnish_UV':Varnish_UV,'Outside_printing':Outside_printing,'DIE_46':DIE_46,'DIE_57':DIE_57,'BOBST':BOBST,'cleaning':cleaning,'BACTED_8S':BACTED_8S,'BACTECHGS':BACTECHGS,'FG':FG,'SBL':SBL,'Manual':Manual,'bind':bind,'finished_goods':finished_goods,'external_adhesive':external_adhesive,'Closed':Closed,'Account':Account,'Invoiced':Invoiced,'Deleted':Deleted})




#.exclude(Ord_states__name__in=['Deleted', 'Finished', 'Closed','حسابات'])  
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Customer, Product, Order

def representative_view(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return render(request, '404.html')  # Render a custom 404 page or handle the error appropriately

    products = Product.objects.filter(Product_Customer=customer)
    
    # Filter orders based on different criteria
    orders = Order.objects.filter(Ord_Product__Product_Customer=customer)\
                      .exclude(Ord_states__name__in=['Deleted', 'Finished', 'Closed', 'حسابات'])\
                      .order_by('-id')


    Closed = Order.objects.filter(Ord_Product__Product_Customer=customer, Ord_states__name__contains='Closed')\
                                  .order_by('-id')
    Invoiced = Order.objects.filter(Ord_Product__Product_Customer=customer, Ord_states__name__contains='حسابات')\
                                    .order_by('-id')
    Account = Order.objects.filter(Ord_Product__Product_Customer=customer, Ord_states__name__contains='Finished')\
                                   .order_by('-id')
    deleted_orders = Order.objects.filter(Ord_Product__Product_Customer=customer, Ord_states__name__contains='Deleted')\
                                   .order_by('-id')
    OrderDeliveryDate = Order.objects.filter(
        ~Q(Ord_states__name__in=['Closed', 'حسابات', 'Finished','Deleted']),Ord_Product__Product_Customer=customer).order_by('-id')


    context = {
        'customer': customer,
        'products': products,
        'orders': orders,
        'Closed': Closed,
        'Invoiced': Invoiced,
        'Account': Account,
        'deleted_orders': deleted_orders,
        'OrderDeliveryDate': OrderDeliveryDate,
    }

    return render(request, 'product/representative/main_taps_representative.html', context)
