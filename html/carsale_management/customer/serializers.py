from rest_framework import serializers
from customer.models import Customer
class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('id','name','address','mobile_no','car_model','carmodel_year','purchased_date','username','password')

