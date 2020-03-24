from django.urls import path

from . import views

urlpatterns = [
    path('', views.solarPV, name='solarPV'),
    path('solarPVReg/',views.solarPVReg,name='solarPVReg'),
    path('solarPVWebform/',views.solarPVWebform,name='solarPVWebform'),
]
