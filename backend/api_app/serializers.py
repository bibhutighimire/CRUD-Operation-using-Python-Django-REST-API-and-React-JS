from rest_framework import serializers
from api_app.models import Patient, HealthCareDetails

""" class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'blood']
 """
class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['patient_id','last_name','first_name','blood'] 

class HealthCareDetailsSerializer(serializers.HyperlinkedModelSerializer):
    fk = PatientSerializer() 
   
    class Meta:
        model = HealthCareDetails
        fields = ['healthcare_id','healthcarenumber', 'physician', 'fk']

