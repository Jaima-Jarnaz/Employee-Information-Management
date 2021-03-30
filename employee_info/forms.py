from django import forms
from .models import Employee,AdminForm
class Admin_Login_Form(forms.ModelForm):
    class Meta:
        model=AdminForm
        fields='__all__'

    

class Employee_Form(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

    
    def __init__(self,*args,**kwargs):
        super(Employee_Form,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label='Select'



