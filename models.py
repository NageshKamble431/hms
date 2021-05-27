
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_patient = models.BooleanField(default = False)
    is_doctor = models.BooleanField(default = False)

class PatientInfo(models.Model):
    patient_name = models.ForeignKey(User, on_delete=models.CASCADE)
    Gender=models.CharField(max_length=20)
    birth_date = models.DateTimeField(null=True,blank=True)
    City  = models.CharField(max_length=50)
    Disease=models.CharField(max_length=250)
    Email=models.EmailField(null=True,blank=True)

class Doctorinfo(models.Model):
    doctor_name = models.ForeignKey(User, on_delete=models.CASCADE)
    Gender=models.CharField(max_length=20)
    birth_date = models.DateTimeField(null=True,blank=True)
    City  = models.CharField(max_length=50)
    Disease_specialist=models.CharField(max_length=250)
    Education=models.CharField(max_length=250)
   # Email=models.EmailField(null=True,blank=True)

class appointment(models.Model):
    patient_name = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(null=True, blank=True)
    Disease = models.CharField(max_length=250)
