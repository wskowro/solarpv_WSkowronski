from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('product', views.ProductView)
router.register('certificate', views.CertificateView)
router.register('service', views.ServiceView)

urlpatterns = [
    path('', views.index, name='solarPV'),
    path('solarPVReg/',views.reg,name='solarPVReg'),
    path('solarPVWebform/',views.webform,name='solarPVWebform'),
    path('api/', include(router.urls))
]