from django.contrib import admin
from .models import Disease,Doctor,Symptoms,Prescription
# Register your models here.
admin.site.register(Disease)
admin.site.register(Doctor)
admin.site.register(Symptoms)
admin.site.register(Prescription)