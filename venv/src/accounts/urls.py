from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('admin/', views.admin, name='admin'),
    path('uniPerson/', views.uniPerson, name='uniPerson'),
    path('outsider/', views.outsider, name='outsider'),
    path('role/', views.role, name='role'),
    path('register/', views.register, name='register'),
    path('register/admin/', views.register_admin, name='admin_registration'),
    path('register/university_person/', views.register_uniPerson, name='university_person_registration'),
    path('register/outsider/', views.register_outsider, name='register_outsider'),
]
