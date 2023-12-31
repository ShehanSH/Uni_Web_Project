"""
URL configuration for Uni_Web_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from inventory_management import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('list_items', views.list_items, name='list_items'),
    path('admin/', admin.site.urls),
   
    path('', views.homemain, name='homemain'),
    path('testchart/', views.testchart, name='testchart'),
    path('', views.slidebar, name='slidebar'),
    
    # path('list_items/', views.list_items, name='list_items'),
    # path('update_items/<str:pk>/', views.update_items, name="update_items"),
    # path('delete_items/<str:pk>/', views.delete_items, name='delete_items'),
    # path('add_items/', views.add_items, name='add_items'),
    # path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    # path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
    # path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),
    # path('reorder_level/<str:pk>/', views.reorder_level, name="reorder_level"),
    # path('accounts/', include('registration.backends.default.urls')),
    # path('list_history/', views.list_history, name='list_history'),
    path('', include('accounts.urls')),
    path('logout/', views.logout_view, name='logout'),
    path('account_lockout/', views.account_lockout_view, name='account_lockout'),
    
    # path('accounts/', include('registration.backends.default.urls')),
    # path('sports_item_req/', include(('sports_item_req.urls', 'sports_item_req'), namespace='sports_item_req')),
   
    # path('chart', chart.home, name='home'),
    # path('inventory_chart/', views.inventory_chart, name='inventory_chart'),
    path('inventory_chart_view/', views.inventory_chart_view, name='inventory_chart_view'),
    path('inventory_chart_view/<int:category_id>/', views.inventory_chart_view, name='inventory_chart_view_filtered'),
    path('inventory_reorder_chart_view/', views.inventory_reorder_chart_view, name='inventory_reorder_chart_view'),
    path('inventory_stock_count_chart_view/', views.inventory_stock_count_chart_view, name='inventory_stock_count_chart_view'),
    path('inventory_reorder_chart_view/<int:category_id>/', views.inventory_reorder_chart_view, name='inventory_reorder_chart_view_filtered'),


    path('supplier_chart_view/', views.supplier_chart_view, name='supplier_chart_view'),
    path('supplier_name_chart/', views.supplier_name_chart, name='supplier_name_chart'),
    path('supply_inventory_stock_over_time/', views.supply_inventory_stock_over_time, name='supply_inventory_stock_over_time'),

    #reports
    # path('inventory_stock_report/', views.inventory_stock_report, name='inventory_stock_report'),
    
    
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('generate_csv/', views.generate_csv, name='generate_csv'),
    path('reorder_report/', views.reorder_report, name='reorder_report'),

    path('generate_pdf2/', views.generate_pdf2, name='generate_pdf2'),
    path('generate_csv2/', views.generate_csv2, name='generate_csv2'),
    path('stock_report/', views.reorder_report2, name='stock_report'),

    path('supply_stock/', views.reorder_report3, name='supply_stock'),
    path('generate_pdf3/', views.generate_pdf3, name='generate_pdf3'),
    path('generate_csv3/', views.generate_csv3, name='generate_csv3'),
    
    # path('generate_pdf_image/', views.generate_pdf_image, name='generate_pdf_image'),

    # path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('', include('sports_items_req.urls')),
    path('', include('ground_booking.urls')),
    # path('select_category/', views.generate_pdf, name='select_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)