from django.urls import path, include
from .import views
app_name = 'patient'
urlpatterns = [
    path('',views.home,name='home' ),
    path('signup/<int:status>',views.signup,name='signup'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor, name='doctor'),
    path('signin/', views.signin, name='signin'),
    path('patientresult/',views.patientresult,name='patientresult'),
    path('patientappointment/',views.patientappointment,name='patientappointment'),
    path('viewappointment/',views.viewappointment,name='viewappointment'),
    path('doctorappointment/',views.doctorappointment,name='doctorappointment'),


    path('logout/', views.logout_user, name='logout'),
    path('addpatientinfo/', views.addpatientinfo, name='addpatientinfo'),
    path('editpatientinfo/', views.editpatientinfo, name='editpatientinfo'),
    path('deletepatientinfo/', views.deletepatientinfo, name='deletepatientinfo'),
    path('showpatientinfo/<int:id>', views.showpatientinfo, name='showpatientinfo'),
    path('showdoctorinfo/', views.showdoctorinfo, name='showdoctorinfo'),
    path('adddoctorinfo/', views.adddoctorinfo, name='adddoctorinfo'),
    path('editdoctorinfo/', views.editdoctorinfo, name='editdoctorinfo'),
    path('deletedoctorinfo/', views.deletedoctorinfo, name='deletedoctorinfo')

]