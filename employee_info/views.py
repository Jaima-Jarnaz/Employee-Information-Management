from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password,make_password
from django.http import HttpResponse
from .forms import *



def index(request):
    if request.method=='POST':
        form=Admin_Login_Form()
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email+password)
        e=AdminForm.objects.get(email=email)
        if e:
            if email==e.email:
                request.session['email']=e.email
                return redirect('employee_list')     
            else: 
                print("sorry")
                return render(request,'index.html',{'form':form})
        else:
            return render(request,'index.html',{'form':form})
        
    else:
        form=Admin_Login_Form()
        print("sorry2")
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





