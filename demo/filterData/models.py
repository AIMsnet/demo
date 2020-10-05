from django.db import models

# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=225)
    emob = models.CharField(max_length=10)
    eadd =  models.CharField(max_length=225)
    pin = models.CharField(max_length=6)
    edept = models.CharField(max_length=125)