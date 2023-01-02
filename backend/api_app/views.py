from django.shortcuts import render
from requests import Response
from rest_framework import viewsets
from api_app.models import Patient, HealthCareDetails
from api_app.serializers import  HealthCareDetailsSerializer, PatientSerializer


def home(request):
    hc=HealthCareDetails.objects.all()
    return render(request, 'home.html',{'hc':hc})

class HealthCareDetailsViewSet(viewsets.ModelViewSet):
    queryset= HealthCareDetails.objects.all()
    serializer_class = HealthCareDetailsSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset= Patient.objects.all()
    serializer_class = PatientSerializer
