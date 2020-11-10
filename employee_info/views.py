from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *


def index(request):
    if request.method=='POST':
        form=Employee_Login_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form=Employee_Login_Form()
    return render(request,'index.html',{'form':form})



def employee_form(request,id=0):
    if request.method=='POST':
        if id==0:
            form=Employee_Form(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=Employee_Form(request.POST,instance=employee)

        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        if id==0:
            form=Employee_Form()
        else:
            employee=Employee.objects.get(pk=id)
            form=Employee_Form(instance=employee)
        return render(request,'employee.html',{'form':form})



def employee_list(request):
    emp_list=Employee.objects.all()
    return render(request,'employee_list.html',{'emp_list':emp_list})

def employee_delete(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/')





