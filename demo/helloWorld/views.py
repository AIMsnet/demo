from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
    return HttpResponse ("hello world")

def add(request):
    print('in add')
    if request.method == 'POST' and "ADD":
        val1 = int(request.POST.get("val1"))
        val2 = int(request.POST.get("val2"))
        print(val1, val2)
        add = val1 + val2
        return render(request, "calculation.html", {"add" : add})
    return render(request, "calculation.html")

def sub(request):
    print('in sub')
    if request.method == 'POST':
        val1 = int(request.POST.get("val3"))
        val2 = int(request.POST.get("val4"))
        print(val1, val2)
        sub = val1 - val2
        return render(request, "calculation.html", {"sub" : sub})
    return render(request, "calculation.html")

def multiply(request):
    print('in multiply')
    if request.method == 'POST':
        val1 = int(request.POST.get("val3"))
        val2 = int(request.POST.get("val4"))
        print(val1, val2)
        multiplication = val1 * val2
        return render(request, "calculation.html", {"multiplication" : multiplication})
    return render(request, "calculation.html")

def div(request):
    print('in div')
    if request.method == 'POST':
        val1 = int(request.POST.get("val3"))
        val2 = int(request.POST.get("val4"))
        print(val1, val2)
        div = val1 / val2
        return render(request, "calculation.html", {"div" : div})
    return render(request, "calculation.html")
