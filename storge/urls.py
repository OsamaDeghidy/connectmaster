from django.urls import path
from . import views

urlpatterns = [  
    path ('tr', views.transaction, name='transaction'),
    path('storge/supplier/', views.supplier_view, name='supplier'),
    path('storge/supplier/add/', views.supplier_add_view, name='supplier_add'),
    path('storge/supplier/update/<int:pk>/', views.supplier_update_view, name='supplier_update'),
    path ('storge/iteam/add/', views.iteam_add_view, name='iteam_add'),
    path ('storge/iteam/', views.iteam_view, name='iteam'),
    path('storge/InStockNumbery/', views.InStockNember_view, name='InStockNumber'),
    path('storge/InStockNumbery/update/<int:pk>/', views.InStockNember_update_view, name='InStockNumber_update'),
    path ('storge/in_stock/<int:pk>/', views.in_stock_view, name='in_stock'),
    path('storge/in_stock/add/<int:pk>/', views.in_stock_add_view, name='in_stock_add'),
    path ('storge/in_stock_supplier/<int:pk>/', views.in_stock_supplier_view, name='in_stock_supplier'),
    path ('storge/custmer/', views.custmer_view, name='custmer'),
    path ('storge/custmer/update/<int:pk>/', views.custmer_update_view, name='custmer_update'),
    path ('storge/Out_StockNumber/', views.Out_StockNumber_view, name='OutStockNumber'),
    path ('storge/Out_StockNumber/update/<int:pk>/', views.Out_StockNumber_update_view, name='OutStockNumber_update'),
   
    path ('storge/out_stock_customer/<int:pk>/', views.out_stock_customer_view, name='out_stock_customer'),

    path ('storge/out_stock/<int:pk>/', views.out_stock_view, name='out_stock'),
    path ('storge/out_stock/add/<int:pk>/', views.out_stock_add_view, name='out_stock_add'),
    
    #path ('sorge/stocks/', views.in_stocks_view, name='stocks'),
    
    path ('storge/out_stock/update/<int:pk>/', views.out_stock_update_view, name='out_stock_update'),
    path ('storge/out_stock_all/', views.out_stock_all_view, name='out_stock_all'),
    path ('storge/item_stock/', views.item_stock_veiw, name='item_stock'),

   ]