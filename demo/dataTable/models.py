from django.db import models

# Create your models here.

class Students(models.Model):
    sname = models.CharField("Student Name",max_length=125)
    smob = models.CharField("Mobile no.", max_length=10)
    saddress = models.CharField("Address", max_length=225)
    pin     = models.IntegerField("Pin Code")

    def __str__(self):
        return self.sname