from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Doctor
from django.forms import ModelForm
from django.contrib.auth import authenticate,get_user_model


#Doctor = get_doctor_model()

# class DoctorForm(forms.Form):
#     # email = forms.EmailField()
#     name = forms.TextInput()
#     password = forms.CharField(widget=forms.PasswordInput())
#     # city = forms.TextInput()
#     # specialization = forms.TextInput()


class DoctorRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    name = forms.TextInput()
    password = forms.CharField(widget=forms.PasswordInput())
    city = forms.TextInput()
    specialization = forms.TextInput()
    doctor_experience = forms.NumberInput()
    cost_per_visit = forms.NumberInput()
    class Meta:
        model = Doctor
        fields = ['name', 'email','password','city','specialization','doctor_experience','cost_per_visit']



# class DoctorLoginForm(forms.Form):
#     username=forms.CharField()
#     password=forms.CharField()

#     def clean(self,*args,**kwargs):
#         username=self.cleaned_data.get('name')
#         password=self.cleaned_data.get('password')

#         if username and password:
#             user=authenticate(username=username,password=password)

#             if not user:
#                 raise forms.ValidationError('User Does Not Exist')

#             if not user.check_password(password):
#                 raise forms.ValidationError('Incorrect Password')

#         return super(DoctorLoginForm, self).clean(*args,**kwargs)

