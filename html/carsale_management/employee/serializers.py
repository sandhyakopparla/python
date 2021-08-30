from rest_framework import serializers
from employee.models import Employee 
class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('id','empcode','name','salary','date_of_joining','designation','username','password')
        

