from email.policy import default
from django.db import models
from django.db import models
import sys,os
path_to_users = os.getcwd() + "/users"
sys.path.insert(0,path_to_users)
from users.forms import UserRegisterForm


class Doctor(models.Model):
    #doctorid = models.IntegerField()
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)
    city= models.CharField(max_length=70,default = "Mumbai")
    specialization= models.CharField(max_length=70,default = "Surgeon")
    doctor_experience= models.IntegerField(default = 0)
    cost_per_visit = models.IntegerField(default = 0)



# Create your models here.
