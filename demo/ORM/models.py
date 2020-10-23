from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

class Scientist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Discovry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    scientist = models.ForeignKey(Scientist, related_name="discovry", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Customer(models.Model):
    name    =   models.CharField(max_length=100)
    mobno   =   models.CharField(max_length=10, null=False, blank=False, unique=True)

class Account(models.Model):
    atype   =   models.CharField(max_length=100)
    accNo   = models.CharField(max_length=10)

class BankDetails(models.Model):
    customer = models.ManyToManyField(Customer)    
    account  = models.ManyToManyField(Account)
    balance =   models.CharField(max_length=6)


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title