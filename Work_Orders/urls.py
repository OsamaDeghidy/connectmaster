from django.urls import path
from . import views
urlpatterns = [
        path('', views.dashboard, name='dashboard'),
        path('sectors/', views.sectors, name='sectors'),
        path('customers/', views.customers, name='customers'),
        path('products/', views.all_products_view, name='products'),
        path('orders/', views.orders, name='orders'),
        path('form/', views.new_customer_all, name='new_customer_all'),
        path('<int:Sector_id>/', views.sector_customers, name='sector_customers' ),
        path('<int:Sector_id>/new', views.new_customer, name='new_customer'),
        path('<int:Sector_id>/<int:Customer_id>/edit/', views.CustomerUpdatedView, name='customer_update'),
        path('<int:Sector_id>/<int:Customer_id>/customer_print', views.customer_print, name='customer_print'),
        path('<int:Sector_id>/<int:Customer_id>', views.customer_products, name='customer_products'),
        path('<int:Sector_id>/<int:Customer_id>/new/', views.new_product, name='new_product'),
        path('<int:Sector_id>/<int:Customer_id>/<int:Product_id>/print', views.print_product, name='print_product'),

        #fro product 
        path('edit_product/<int:sector_id>/<int:customer_id>/<int:product_id>/', views.edit_product, name='edit_product'),   

        path('forbidden_page/', views.forbidden_page, name='forbidden_page'),
        

        path('customer/<int:customer_id>/re/', views.representative_view, name='representative_view'),


        
        
]
