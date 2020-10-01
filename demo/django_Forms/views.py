from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Client
from .forms import ClientForm

# Create your views here.

def create_View(request):
    form = ClientForm()
    clients = Client.objects.all()
    print(" a ")
    if request.method == 'POST':
        form = ClientForm(request.POST)
        print(" b ")
        if form.is_valid():
            print(" c ")
            form.save()
            messages.success(request, "Client Registered")
            return redirect('/forms/', {'clients' : clients})
        else:
            messages.error(request, "Please Re-try Something Went Wrong")
            print(form.errors.as_json)
            print('d')
            return redirect('/forms/')
    else:
        return render(request, 'client.html', {'form' : form, 'clients' : clients})

def edit(request, id):
    clients = Client.objects.all()
    client = Client.objects.get(id = id)
    form = ClientForm(instance=client)    
    return render(request, 'clientUpdate.html', {'form' : form, 'clients' : clients})

def update_View(request):
    clients = Client.objects.all()
    print('view')

    # client = Client.objects.get(id = id)
    # form = ClientForm(instance=client) 
    
    if request.method == 'POST':
        form = ClientForm(request.POST)
        print("Before form Valid")
        if form.is_valid():
            print('in', form.cleaned_data)
            print("Update View", form.cleaned_data['cmobno'])
            clientUpdate = Client.objects.get(cmobno = form.cleaned_data['cmobno'])
            clientUpdate.cname = form.cleaned_data['cname']
            clientUpdate.cmobno = form.cleaned_data['cmobno']
            clientUpdate.address = form.cleaned_data['cmobno']
            clientUpdate.pincode = form.cleaned_data['pincode']
            clientUpdate.save()

            messages.success(request, "Client Updated")
            return redirect('/forms/', {'clients' : clients})
        else:
            messages.error(request, "Please Re-try Something Went Wrong")
            print(form.errors.as_json)
            print('d')
            return redirect('/forms/')    
    return render(request, 'client.html', {'form' : form, 'clients' : clients})

def delete_View(request, id):
    form = ClientForm()
    clients = Client.objects.all()
    client = Client.objects.get(id = id)
    client.delete()
    return render(request, 'client.html', {'form' : form, 'clients' : clients})
