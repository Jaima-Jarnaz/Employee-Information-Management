from django.urls import path
from . import views
from .views import *

urlpatterns=[
    path("", views.index,name="index"),
    path("employee_form/", views.employee_form,name="employee_form"),
    path('<int:id>/', views.employee_form,name="employee_update"),
    path("employee_list/", views.employee_list,name="employee_list"),
    path('<int:id>', views.employee_delete,name="employee_delete"),

]