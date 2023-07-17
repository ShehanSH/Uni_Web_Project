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


urlpatterns = [
    path('list_items', views.list_items, name='list_items'),
    path('admin/', admin.site.urls),
   
    path('', views.homemain, name='homemain'),
    
    path('list_items/', views.list_items, name='list_items'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('delete_items/<str:pk>/', views.delete_items, name='delete_items'),
    path('add_items/', views.add_items, name='add_items'),
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
    path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),
    path('reorder_level/<str:pk>/', views.reorder_level, name="reorder_level"),
    # path('accounts/', include('registration.backends.default.urls')),
    path('list_history/', views.list_history, name='list_history'),
    path('', include('accounts.urls')),

    
    # path('accounts/', include('registration.backends.default.urls')),
    # path('sports_item_req/', include(('sports_item_req.urls', 'sports_item_req'), namespace='sports_item_req')),
   
    path('home', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    
    path('', include('sports_items_req.urls')),
    path('', include('ground_booking.urls')),
]
