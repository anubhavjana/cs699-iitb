from django.db import models


from django.db import models

from django.http import request

class Appointment(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    doctor = models.CharField(max_length=70,default="automatic selection")
    status = models.CharField(max_length=70,default="Pending")
    
    # doctor_experience = models.CharField(max_length=70,default="Pending")
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)
    def __str__(self):

        return self.first_name

    

    class Meta:

        ordering = ["-sent_date"]
# Create your models here.
