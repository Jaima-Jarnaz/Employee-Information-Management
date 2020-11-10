from django.contrib import admin
from .models import Employee,Designations

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','emp_code','position','address','mobile']

#class DesignationsAdmin(admin.ModelAdmin):
    #list_display=['positon']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Designations)