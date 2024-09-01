from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:Sector_id>/<int:Customer_id>/<int:Product_id>', views.product_orders, name='product_orders'),
    path('<int:Sector_id>/<int:Customer_id>/<int:Product_id>/new', views.new_order, name='new_order'),
    path('<int:Sector_id>/<int:Customer_id>/<int:Product_id>/<int:Order_id>/edit', views.OrderUpdatedView, name='order_update'),
    path('<int:Sector_id>/<int:Customer_id>/<int:Product_id>/<int:Order_id>/status', views.OrderStatusupdate, name='order_status_update'),
    path('<int:Order_id>/print', views.print_order, name='print_order'),


    #order status url name = open_order
    path('Prepressied', views.Prepressied, name='Prepressied'),
    path('paperpreprat', views.paperpreprat_veiw, name='paperpreprat'),
    path('In_progress', views.In_progress, name='In_progress'),
    path('PrintingServics', views.PrintingServics_veiw, name='PrintingServics'),
    path('diecvting', views.diecvting_veiw, name='diecvting'),
    path('gluing', views.gluing_veiw, name='gluing'),
    
    path('Under_Delivery/', views.Under_Delivery, name='Under_Delivery'),
    path('Finished/c', views.Closed, name='Closed'),#for closed
    path('In_voiced', views.Fenished, name='Fenished'),#for fenished
    path('closed/', views.In_voiced, name='In_voiced'),#for invoiced
    path('Deleted', views.Deleted, name='Deleted'),
    path('<int:Order_id>/details', views.Order_details, name='Order_details'),
    path('new_corrective_action/<int:product_id>/', views.new_corrective_action, name='new_corrective_action'),
    path('corrective_action/<int:corrective_action_id>/edit/', views.edit_corrective_action, name='edit_corrective_action'),
    path('order-delivery-date/list/', views.OrderDeliveryDateveiw_list, name='order_delivery_date_list'),
    path('order-delivery-date/<int:order_id>/', views.edit_order_delivery_date, name='order_delivery_date_update'),
    path('order/<int:order_id>/edit-rdd/', views.edit_rdd, name='edit_rdd'),
    path('order/<int:order_id>/edit-edd/', views.edit_edd, name='edit_edd'),
    path('Open_orders', views.opend_orders, name='opend_orders'),
    path('orders/filter/<path:representative_name>/',views.filter_orders_by_representative, name='filter_orders_by_representative'),]

# Order\urls.py
#{% url 'filter_orders_by_representative'  Order.Ord_Product.customer_representative %}