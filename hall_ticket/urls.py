"""hall_ticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from app.views import*
from hallticket.views import*


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # path('create_admin/', create_admin, name='create_admin'),
    # path('admin_requests/', admin_requests, name='admin_requests'),
    path('superadmin_login', superadmin_login, name='superadmin_login'),
    path('superadmin/profile/', superadmin_profile, name='superadmin_profile'),
    path('superadmin/new-admin/', new_admin, name='create_admin'),
    path('admin_login/', admin_login, name='admin_login'),
    path('admin_profile/',admin_profile, name='admin_profile'),
    path('admin/unauthorized/', unauthorized, name='unauthorized'),
    path('admin/login_mismatch/',login_mismatch, name='login_mismatch'),

          path('new_hall_ticket_registration/',new_hall_ticket_registration, name='new_hall_ticket_registration'),
          path('new_student_registration/',new_student_registration, name='new_student_registration'),
          path('student_login/', student_login, name='student_login'),
          path('student_profile/', student_profile, name='student_profile'),
          path('generate_hall_ticket/',generate_hall_ticket, name='generate_hall_ticket'),
        #    path('student_login/', CustomLoginView.as_view(), name='student_login'),
           path('dashboard/', student_dashboard, name='student_dashboard'),
         path('profile/', student_profile, name='student_profile'),



         ##unauthorized / mismatch 

    path('admin/login_mismatch/index',index, name=' admin/login_mismatch/index'),
    path('admin/unauthorized/index',index, name=' admin/unauthorized/index'),

       

]               
