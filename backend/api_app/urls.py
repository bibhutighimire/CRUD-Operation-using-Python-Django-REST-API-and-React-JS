from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_app.views import HealthCareDetailsViewSet, PatientViewSet
from api_app import views

router = routers.DefaultRouter()
router.register(r'patient', PatientViewSet),
router.register(r'healthcare', HealthCareDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pp/', views.home, name = 'pp')
    
]