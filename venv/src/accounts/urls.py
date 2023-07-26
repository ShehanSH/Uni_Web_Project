from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth import views as auth_views


urlpatterns = [
#     path('accounts/login/', views.login, name='login'),
#     path('admin/', views.admin, name='admin'),
#     path('uni_student/', views.uni_student, name='uni_student'),
#     path('outsider/', views.outsider, name='outsider'),

#     path('index/', views.index, name='index'),
# #    path('uni_registration/', views.uni_registration, name='uni_registration'),
#     path('outsider_registration/', views.outsider_registration, name='outsider_registration'),
#     # path('register/admin/', views.register_admin, name='admin_registration'),
#     # path('register/university_person/', views.register_uniPerson, name='university_person_registration'),
#     # path('register/outsider/', views.register_outsider, name='register_outsider'),
#     # path('register/university_person/', views.university_person_register, name='university_person_register'),
#     path('uni_registration/', views.uni_registration, name='uni_registration'),
#     path('uni_staff_registration/', views.uni_staff_registration, name='uni_staff_registration'),
#     path('test2/', views.test2, name='test'),
   
    
    path('login/', views.login_view, name='login'),
    # path('register/', views.registration_view, name='register'),
    # path('register/', views.registration_view, name='register'),
    # path('home2nd/', views.home2nd, name='home2nd'),
    path('role/', views.role, name='role'),
    path('uni_student_registration/', views.uni_student_registration, name='uni_student_registration'),
    path('uni_staff_registration/', views.uni_staff_registration, name='uni_staff_registration'),
    path('outsider_registration/', views.outsider_registration, name='outsider_registration'),
    # path('homemain', views.homemain, name='homemain'),

    path("password_change", views.password_change, name="password_change"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),

    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.edit_user_profile, name='edit_user_profile'),
    path('profile/delete/', views.delete_user_profile, name='delete_user_profile'),
]
