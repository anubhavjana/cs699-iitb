
from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_view


urlpatterns = [
   
    path('',views.home,name='doctorhome'),
    #path('register/', views.register, name='register'),
    path('profile/', views.profile, name='doctorprofile'),
    path('login/', auth_view.LoginView.as_view(template_name='doctors/login.html'), name="doctorlogin"),
    path('register/', views.register, name="doctorregister"),
    # path('logout/', views.logout_view,  name="doctorlogout"),
    # path('login/', views.login,  name="doctorlogin"),

    path('logout/', auth_view.LogoutView.as_view(template_name='doctors/logout.html'), name="doctorlogout"),
    # path('book/', views.book, name='book'),
    # path('appointment/', views.view_doctor_appointment, name='appointmentdoctor'),
    path('appointment/', ManageAppointmentTemplateView.as_view(), name='appointmentdoctor'),
    path('addinfo/', views.addinforequest, name='addinfo'),


]
