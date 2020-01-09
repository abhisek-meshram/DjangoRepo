from django.db import models
from django.template.defaultfilters import default

# Create your models here.
class DeviceReg(models.Model):
    deviceid= models.CharField(max_length=20)
    username= models.CharField(max_length=30)
    email=models.EmailField()  
    passwd= models.CharField(max_length=20)
    contact= models.CharField(max_length=15)
    
    
    class Meta:
        db_table="devicereg" 
    