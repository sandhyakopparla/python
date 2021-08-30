from django.db import models
class Employee(models.Model):
    empcode=models.IntegerField(max_length=50)
    name=models.CharField(max_length=50)
    salary=models.CharField(max_length=50)
    date_of_joinig=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    
