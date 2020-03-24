# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'solarpv/solarPV.html')

def index(request):
    return render(request, 'solarpv/solarPVReg.html')

def index(request):
    return render(request, 'solarpv/solarPVWebform.html')
