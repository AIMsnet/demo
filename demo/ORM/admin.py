from django.contrib import admin

from .models import Scientist, Discovry,Customer, Account, BankDetails, Author, Book
# Register your models here.

admin.site.register(Scientist)
admin.site.register(Discovry)
admin.site.register(Author)
admin.site.register(Book)

admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(BankDetails)



