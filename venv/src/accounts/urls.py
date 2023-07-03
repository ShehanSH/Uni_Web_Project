from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin, name='admin'),
    path('uniPerson/', views.uniPerson, name='uniPerson'),
    path('outsider/', views.outsider, name='outsider'),
]
