from django.shortcuts import render
from .models import Employee

# Create your views here.

def filterDate(request):
    employees = Employee.objects.all()
    if request.method == "POST":
        dept = request.POST.get('selectDept')
        print(dept)
        employees = Employee.objects.filter(edept = dept)

        return render(request, 'dataFilter.html', {'employees' : employees})

    else:
        return render(request, 'dataFilter.html', {'employees' : employees})