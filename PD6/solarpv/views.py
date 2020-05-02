from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .models import Certificate
from .models import Service
from .serializers import ProductSerializer
from .serializers import CertificateSerializer
from .serializers import ServiceSerializer

def index(request):
    return render(request, 'solarpv/solarPV.html')

def reg(request):
    return render(request, 'solarpv/solarPVReg.html')

def webform(request):
    return render(request, 'solarpv/solarPVWebform.html')

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CertificateView(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

