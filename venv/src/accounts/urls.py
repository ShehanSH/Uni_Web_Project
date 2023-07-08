from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('admin/', views.admin, name='admin'),
    path('uniPerson/', views.uniPerson, name='uniPerson'),
    path('outsider/', views.outsider, name='outsider'),
    path('role/', views.role, name='role'),
    
#    path('uni_registration/', views.uni_registration, name='uni_registration'),
    path('outsider_registration/', views.outsider_registration, name='outsider_registration'),
    # path('register/admin/', views.register_admin, name='admin_registration'),
    # path('register/university_person/', views.register_uniPerson, name='university_person_registration'),
    # path('register/outsider/', views.register_outsider, name='register_outsider'),
    # path('register/university_person/', views.university_person_register, name='university_person_register'),
    path('uni_registration/', views.uni_registration, name='uni_registration'),
    path('uni_staff_registration/', views.uni_staff_registration, name='uni_staff_registration'),
    path('test2/', views.test2, name='test'),

]
