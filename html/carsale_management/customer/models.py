from django.db import models
class Customer(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobile_no=models.BigIntegerField()
    car_model=models.CharField(max_length=50)
    carmodel_year=models.CharField(max_length=50)
    purchased_date=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)