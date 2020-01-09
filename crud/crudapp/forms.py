from .models import DeviceReg
from django import forms 

class DeviceForm(forms.ModelForm):
     class Meta:
         model=DeviceReg
         fields='__all__'