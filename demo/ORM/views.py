from django.shortcuts import render
from .models import Scientist, Discovry, Customer, Account, BankDetails, Author, Book
# Create your views here.

def oneToMany(request):
    scientists = Scientist.objects.all()
    return render(request, "oneToMany.html", {'scientists': scientists})

def showDiscovries(request, id):
    scientists = Scientist.objects.all()
    discovries   = Discovry.objects.filter(scientist = id)
    return render(request, "oneToMany.html", {'scientists': scientists, 'discovries':discovries})


def manyToMany(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    return render (request, "manyToMany.html", {'authors' : authors, 'books': books})

def showBook(request, id):
    authors = Author.objects.all()
    books = Book.objects.filter(author = id)
    return render (request, "manyToMany.html", {'authors' : authors, 'books': books})

def showAuthors(request, id):
    authors = Author.objects.filter(book = id)
    books = Book.objects.all()
    return render (request, "manyToMany.html", {'authors' : authors, 'books': books})

