from django.shortcuts import render , redirect
from .forms import DeviceForm
from .models import DeviceReg
# Create your views here.


def index(request):
    return render(request,'index.html')

def create(request):  
    if request.method == "POST":
        form = DeviceForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass
    else:  
        form = DeviceForm()  
    return render(request,'create.html',{'form':form})


def show(request):  
    deviceData = DeviceReg.objects.all()  
    return render(request,"show.html",{'deviceData': deviceData})  



def edit(request,id):
    deviceData = DeviceReg.objects.get(id=id)
    return render(request,'edit.html', {'deviceData': deviceData})  


def update(request,id):  
    deviceData = DeviceReg.objects.get(id=id)  
    form = DeviceForm(request.POST, instance = deviceData)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'deviceData': deviceData})  


def delete(request,id):  
    device = DeviceReg.objects.get(id=id)  
    device.delete()  
    return redirect("/show")