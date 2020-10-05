from django.shortcuts import render
from .models import Students
# Create your views here.

def showTable(request):
    students = Students.objects.all()
    return render(request, 'dataTable.html', {'students' : students})