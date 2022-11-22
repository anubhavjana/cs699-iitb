
from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_view


urlpatterns = [
   
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('view/', views.view, name='view'),
    path('viewappointment/', views.view_user_appointment, name='viewappointment'),
    path('appointment/', views.appointment, name='userappointment'),
    path('viewcost/', views.view_cost, name='viewcost'),
    path('cancelbooking/', CancelAppointmentTemplateView.as_view(), name='cancelappointment'),

]
