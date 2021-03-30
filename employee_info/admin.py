from .models import Employee,Designations,AdminForm
from django.contrib import admin

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','emp_code','position','address','mobile']

#class DesignationsAdmin(admin.ModelAdmin):
    #list_display=['positon']
class AdminFormLOGIN(admin.ModelAdmin):
    list_display=['email','password']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Designations)
admin.site.register(AdminForm,AdminFormLOGIN)