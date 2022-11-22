from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
import datetime

from .models import Appointment


class UserRegisterForm(UserCreationForm):
    email = forms.EmailInput()
    # type = forms.TextInput()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class AppointmentForm(ModelForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    phone = forms.TextInput()
    email = forms.EmailField()
    request = forms.TextInput()
    doctor = forms.TextInput()
    
    
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name','email','phone','request','doctor']