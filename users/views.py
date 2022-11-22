from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,AppointmentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Appointment
import os 
import sys
path_to_doctor = os.getcwd() + "/doctors"
sys.path.insert(0,path_to_doctor)
from doctors.models import Doctor
from .utils import get_plot
from django.core.mail import EmailMessage, message,send_mail
from django.conf import settings
from django.contrib import messages


from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template

import datetime



def home(request):
    # return HttpResponse("<h1>Home Users</h1>")

    return render(request,'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #firstname = form.cleaned_data.get('firstname')
            #lastname = form.cleaned_data.get('lastname')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')

#@login_required()
def view(request):
    doctor_list = Doctor.objects.all()
    
    return render(request,'users/view.html',{'doctor_list': doctor_list})

@login_required()
def view_user_appointment(request):
    # appointment_id = request.POST.get("appointment-id")
    appointment_list = Appointment.objects.all()
    # appointment = Appointment.objects.get(id=appointment_id)
    # appointment.delete()
    doctors = Doctor.objects.all()
    print(appointment_list)
    names = []
    for a in appointment_list:
        names.append(a.first_name)
    # print(names)
    context = {'appointment_list': appointment_list,'names':names}
    return render(request,'users/viewappointment.html',context)

@login_required()
def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('first_name')
            messages.success(request, f'Hi  {name}, your appointment was submitted successfully')
            return redirect('home')
    else:
        form = AppointmentForm()

    return render(request, 'users/appointment.html', {'form': form})
    
    #return render(request,'users/appointment.html')

def view_cost(request):

    doctors= Doctor.objects.all()
    doctor_names = [d.name for d in doctors ]
    cost_per_visit = [d.cost_per_visit for d in doctors ]
    experience = [d.doctor_experience for d in doctors ]
    chart = get_plot(doctor_names,cost_per_visit,'Doctors vs Cost per visit','Doctor','Cost(in Rs.)')
    chart1 = get_plot(doctor_names,experience,'Doctors vs Experience (in years)','Doctor','Experience (in years)')
    return render(request,'users/cost.html',{'chart':chart,'chart1':chart1})


class CancelAppointmentTemplateView(ListView):
    template_name = "users/cancelbooking.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    # paginate_by = 3


    def post(self,request):
        # date = request.POST.get("date")
        
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        
        appointment.delete()
        # data = {
        #     "fname":appointment.first_name,
        #     "date":date,
        # }

        # # message = get_template('doctors/ManageAppointmentTemplateViewemail.html').render(data)
        # email = EmailMessage(
        #     "About your appointment",
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [appointment.email],
        # )
        # email.content_subtype = "html"
        # print(settings.EMAIL_HOST_USER)
        # # send_mail("About your appointment",message,settings.EMAIL_HOST_USER,[appointment.email],fail_silently=False)

        messages.add_message(request, messages.SUCCESS, f"You cancelled the appointment of {appointment.doctor}")
        
        return redirect('home')


