
from django.db import models


# Create your models here.
class Disease(models.Model):
    name_disease=models.CharField(max_length=100)
    symptom1=models.CharField(max_length=100,default="null")
    symptom2=models.CharField(max_length=100,default="null")
    symptom3=models.CharField(max_length=100,default="null")
    symptom4=models.CharField(max_length=100,default="null")
    symptom5=models.CharField(max_length=100,default="null")
    def __str__(self) -> str:
        return str(f"{self.id} = {self.name_disease}")



class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialist=models.CharField(max_length=100)
    free=models.IntegerField()
    image=models.ImageField(upload_to='doctor')
class Symptoms(models.Model):
    name=models.CharField(max_length=123)
    def __str__(self) -> str:
        return str(f"{self.name}")

class Prescription(models.Model):
    f_name=models.CharField(max_length=120)
    phone=models.CharField(max_length=123)
    doctor=models.CharField(max_length=120)
    def __str__(self) -> str:
        return str(f"{self.f_name}")

