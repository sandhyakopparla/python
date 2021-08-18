from rest_framework import serializers
from employee.models import Employee
class EmployeeSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields =('name','designation','salary','company')
        