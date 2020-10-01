from django.db import models

# Create your models here.


class Client(models.Model):
    cname   = models.CharField("Client Name", max_length=100, null=False)
    cmobno  = models.CharField("Mobile No",max_length=10,  null=False)
    address = models.CharField("Address", max_length=125)
    pincode = models.CharField("Pin", max_length=6, null=False)
    
    def __str__(self): 
        return self.cname