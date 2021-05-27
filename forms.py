from .models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm, UserCreationForm
from django.conf import settings
import datetime
from datetime import datetime, time, date, timedelta
min_date = date.today() - timedelta(50*365)
today = date.today() - timedelta(18*365)

class UserSignupForm(UserCreationForm):
    #username = forms.EmailField(label="Email address")
   # first_name = forms.CharField(max_length=30, label="First Name")
    #last_name = forms.CharField(max_length=30, label="last Name")



    class Meta:
        model = User
        fields = ["username", "password1", "password2", 'first_name','last_name','email']
        exclude = ['is_patient', 'is_doctor','is_admin']

class UserSigninForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

class PatientInfoForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                            attrs={'class': 'form-control datepicker', 'min': min_date,
                                                                   'max': today, 'value': today, 'type': 'date'}),
                                 )
    class Meta:
        model = PatientInfo
        fields = "__all__"
        exclude = ['patient_name']

class DoctorInfoForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                            attrs={'class': 'form-control datepicker', 'min': min_date,
                                                                   'max': today, 'value': today, 'type': 'date'}),
                                 )
    class Meta:
        model = Doctorinfo
        fields = "__all__"
        exclude = ['doctor_name']

class appointmentinfo(forms.ModelForm):
    appointment_date = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                            attrs={'class': 'form-control datepicker', 'min': min_date,
                                                                   'max': today, 'value': today, 'type': 'date'}),
                                 )
    class Meta:
        model = appointment
        fields = "__all__"
        exclude = ['patient_name']