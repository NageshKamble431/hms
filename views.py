from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    information = User.objects.all()
    return render(request, 'home.html', locals())

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                #  request.session['user_id'] = user.pk
                if user.is_patient:
                    information = PatientInfo.objects.filter(patient_name=user)
                    if len(information) > 0:
                        patient_name= information[0]
                        return render(request, 'patient.html', locals())
                    else:
                        form = PatientInfoForm()
                        return render(request, 'addpatientinfo.html', locals())
                else:
                    if user.is_doctor:
                        information = Doctorinfo.objects.filter(doctor_name=user)
                        if len(information) > 0:
                            patient_name = information[0]
                            return render(request, 'doctor.html', locals())
                        else:
                            form = DoctorInfoForm()
                            return render(request, 'adddoctorinfo.html', locals())

            else:
                return HttpResponse("Account is not active")
        else:
            return HttpResponse('****Invalid User****')

    else:
        form = UserSigninForm()
    return render(request, 'signin.html', locals())




def signup(request, status):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if status == 1:
                user.is_patient = True
            elif status == 2:
                user.is_doctor = True


            user.save()
            return redirect('patient:home')
            '''

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = user.pk
                if user.is_patient:
                    return HttpResponse('You are patient')
                elif user.is_doctor:
                    return HttpResponse('You are doctor')
                elif user.is_admin:  
                    return HttpResponse('You are Admin')      

            else:
                return HttpResponse("Account not active")
            '''
        else:
            return HttpResponse("Please Provide Valid Details")

    else:
        if status == 1:
            status = "patient"
        elif status == 2:
            status = "doctor"
        form = UserSignupForm()
    return render(request, 'signup.html', locals())


def logout_user(request):
    # del request.session['user_id']
    request.session.flush()
    logout(request)
    return redirect('patient:home')


def addpatientinfo(request):
    form = PatientInfoForm(request.POST)
    patient = User.objects.get(id=request.user.id)
    if form.is_valid():
        user = form.save(commit=False)
        user.patient_name = patient
        user.save()
        return render(request, 'patient.html', locals())
    else:
        form = PatientInfoForm()
        return render(request, 'addpatientinfo.html', locals())

def adddoctorinfo(request):
    form = DoctorInfoForm(request.POST)
    doctor = User.objects.get(id=request.user.id)
    if form.is_valid():
        user = form.save(commit=False)
        user.doctor_name = doctor
        user.save()
        return HttpResponse("Sucessfully Updated Your Data")
    else:
        return HttpResponse("Please Supply Valid Details")

def editpatientinfo(request):
    object = PatientInfo.objects.filter(patient_name=request.user)[0]
    if request.method == 'POST':

        form = PatientInfoForm(request.POST,instance=object)
        if form.is_valid():
            form.save()
            patients = PatientInfo.objects.filter(patient_name=request.user)
            #return HttpResponse('you are here')
            return render(request,'showpatientinfo.html',locals())
    else:

        form = PatientInfoForm(instance=object)
    return render(request,'editpatientinfo.html',locals())

def editdoctorinfo(request):
    if request.method == 'POST':
        object = Doctorinfo.objects.get(doctor_name=request.user)
        form = DoctorInfoForm(request.POST,instance=object)
        if form.is_valid():
            form.save()
            information = Doctorinfo.objects.filter(doctor_name=request.user)
            return render(request,'showdoctorinfo.html',locals())
    else:
        object = Doctorinfo.objects.get(doctor_name=request.user)
        form = DoctorInfoForm(instance=object)
    return render(request,'editdoctorinfo.html',locals())


def deletepatientinfo(request):
    object = PatientInfo.objects.get(patient_name=request.user)
    object.delete()
    return HttpResponse(" ***Your Data Is Deleted**")

def deletedoctorinfo(request):
    object = Doctorinfo.objects.get(doctor_name=request.user)
    object.delete()
    return HttpResponse(" ***Your Data Is Deleted**")

def showpatientinfo(request,id):
    if request.user.is_patient:
        patient = User.objects.get(id=id)
        patients = PatientInfo.objects.filter(patient_name=patient)
    else:
        patient=User.objects.get(id=id)
        patients = PatientInfo.objects.filter(patient_name=patient)
    return render(request, 'showpatientinfo.html',locals())

def showdoctorinfo(request):
    information = Doctorinfo.objects.filter(doctor_name=request.user)
    return render(request, 'showdoctorinfo.html',locals())

def patient(request):
    if request.user.is_doctor:
        information = PatientInfo.objects.all()
    else:
        information = PatientInfo.objects.filter(patient_name=request.user)
    return  render(request,'patient.html',locals())

def patientresult(request):
    return  render(request,'patientresult.html')

def patientappointment(request):
    form = appointmentinfo(request.POST)
    patient = User.objects.filter(id=request.user.id)[0]
    if form.is_valid():
        user = form.save(commit=False)
        user.patient_name = patient
        user.save()
        return render(request, 'viewappointment.html', locals())
    else:
        form = appointmentinfo()

    return render(request, 'patientappointment.html', locals())

def viewappointment(request):
    object = appointment.objects.filter(patient_name=request.user)[0]

    if request.method == 'POST':
        print('lllaala')
        form = appointmentinfo(request.POST,instance=object)
        if form.is_valid():
            form.save()
            patient = appointment.objects.filter(patient_name=request.user)
            #return HttpResponse('you are here')
            return render(request,'viewappointment.html',locals())
    else:

        form = appointmentinfo()
    #return HttpResponse('you are herehggjggj')
    return render(request,'patient.html',locals())

def doctorappointment (request):
    return HttpResponse('welcome here')


def doctor(request):
    information = Doctorinfo.objects.filter(doctor_name=request.user)
    return  render(request,'doctor.html',locals())