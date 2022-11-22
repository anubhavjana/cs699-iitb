
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from requests import request
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, message,send_mail
from django.conf import settings
from django.contrib import messages

from django.contrib.auth import login,logout,authenticate
import os 
import sys
path_to_user= os.getcwd() + "/users"
sys.path.insert(0,path_to_user)

from users.forms import UserRegisterForm
from users.models import Appointment

from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template


def home(request):
    # return HttpResponse("<h1>Home Users</h1>")

    return render(request,'doctors/home.html')

def login_view2(request):
    next = request.GET.get('next')
    form = DoctorRegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "doctors/login.html", context)


def register_view2(request):
    next = request.GET.get('next')
    form = DoctorRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "doctors/signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')

@login_required()
def addinforequest(request):
    if request.method == "POST":
        form = DoctorRegisterForm(request.POST)
        form.cost_per_visit = 2 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi your info account was added successfully')
            return redirect('doctorhome')

    else:
        form = DoctorRegisterForm()
        
    return render(request, 'doctors/addinfo.html', {'form': form})
            



def register(request):
    if request.method == "POST":
        # doctor= Doctor()
        form = UserRegisterForm(request.POST)
        # form1 = DoctorRegisterForm(request.POST)
        # form1.save()
        # city = form1.cleaned_data.get('city')
        # specialization = form1.cleaned_data.get('specialization')
        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data.get('username')
        #     password = form.cleaned_data.get('password1')
        #     email = form.cleaned_data.get('email')
        #     doctor = Doctor(name=username,email=email,password=password,city=city,specialization=specialization)
        #     doctor.save()
        #     messages.success(request, f'Hi Dr. {username}, your account was created successfully')

        #     return redirect('doctorhome')
        

            
        
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, f'Hi Dr. {name}, your account was created successfully. Go ahead to add your info')
            return redirect('doctorhome')
    else:
        form = UserRegisterForm()
        # form = UserRegisterForm()

    return render(request, 'doctors/register.html', {'form': form})

def login3(request):
    doctor_list = Doctor.objects.all()
    form = DoctorRegisterForm(request.POST)
    print(doctor_list)
    doctor_info={}
    for doctor in doctor_list:
        doctor_info[doctor.name]=doctor.password
    # form = DoctorLoginForm(request.POST)
    
    if form.is_valid():
        print("Inside form")
        name = form.cleaned_data.get('name')
        print("NAME",name)
    # print(request.POST)
    #print("FORM-----",form.name)
    print(doctor_info)

    return render(request, "doctors/login.html",{'form': form})
    # form = DoctorLoginForm(request.POST)
    
    # if form.is_valid():

    #     username = form.cleaned_data.get('name')
    #     password = form.cleaned_data.get('password')
    #     print(username,password)
    #     user = authenticate(username=username, password=password)
    #     login(request, user)

        

    #     return render(request, "doctors/home.html",{'form': form})

    

@login_required()
def view_doctor_appointment(request):
    
    appointment_list = Appointment.objects.all()
    
    print(appointment_list)
    doctor_names = []
    for a in appointment_list:
        doctor_names.append(a.doctor)
    # print(names)
    context = {'appointment_list': appointment_list,'names':doctor_names}
    return render(request,'doctors/viewappointment.html',context)

#@login_required()
def profile(request):

    return render(request, 'doctors/profile.html')
#@login_required()
def book(request):
    return render(request,'doctors/book.html')

#@login_required()
def appointment(request):
    return render(request,'doctors/appointment.html')

class ManageAppointmentTemplateView(ListView):
    template_name = "doctors/viewappointment.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    # paginate_by = 3


    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.status = "Accepted"
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()
        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('doctors/email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        print(settings.EMAIL_HOST_USER)
        # send_mail("About your appointment",message,settings.EMAIL_HOST_USER,[appointment.email],fail_silently=False)

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        
        return redirect('doctorhome')






