from django.forms import ModelForm
from django import forms
from .models import Patients

class PatientForm(ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'

class SurgeonForm(ModelForm):
    class Meta:
        model = Patients
        fields = ['surgery']