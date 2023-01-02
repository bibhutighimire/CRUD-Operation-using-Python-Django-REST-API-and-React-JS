from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    blood= models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class HealthCareDetails(models.Model):
    healthcare_id = models.BigAutoField(primary_key=True)
    healthcarenumber = models.BigIntegerField(unique=True)
    physician = models.CharField(max_length=50)
    fk = models.ForeignKey(Patient, related_name='patient_healthcare', on_delete=models.CASCADE)

