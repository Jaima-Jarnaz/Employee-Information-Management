from django.db import models

class AdminForm(models.Model):
    email=models.EmailField()
    password=models.IntegerField()

class Designations(models.Model):
    position=models.CharField(max_length=100)

    def __str__(self):
        return self.position

class Employee(models.Model):
    name=models.CharField(max_length=200)
    emp_code=models.IntegerField()
    position=models.ForeignKey(Designations,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    mobile=models.IntegerField()

