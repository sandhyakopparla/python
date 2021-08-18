from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from employee.serializers import EmployeeSerilizer
from employee.models import Employee
from rest_framework.parsers import JSONParser 
from rest_framework import status
@csrf_exempt
def employee_details(request,fetchid):
    try:
        employees=Employee.objects.get(id=fetchid)
        if(request.method =="GET"):
            employee_serializer=EmployeeSerilizer(employees)
            return JsonResponse(employee_serializer.data,safe=False,status=status.HTTP_200_OK)

        if (request.method=="DELETE"):
            employees.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            employee_serializer=EmployeeSerilizer(employees,data=mydict)
            if(employee_serializer.is_valid()):
                employee_serializer.save()
                return JsonResponse(employee_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(employee_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Employee.DoesNotExist:
        return HttpResponse("invalid Employee Id",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def employee_list(request):
    if(request.method=="GET"):
        employees=Employee.objects.all()
        employee_serializer=EmployeeSerilizer(employees,many=True)
        return JsonResponse(employee_serializer.data,safe=False)

@csrf_exempt 
def employeePage(request):
    if(request.method=="POST"):
        # getEmpName=request.POST.get("name")
        # getDesig=request.POST.get("designation")
        # getSalary=request.POST.get("salary")
        # getCompany=request.POST.get("company")
        # mydict={"name":getEmpName,"designation":getDesig,"salary":getSalary,"company":getCompany}
        mydict=JSONParser().parse(request)
        employee_serialize=EmployeeSerilizer(data=mydict)
        if(employee_serialize.is_valid()):
            employee_serialize.save()
            # return HttpResponse(employee_srialize)
            return JsonResponse(employee_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
        # result=json.dumps(mydict)
        # return HttpResponse(result)
    else:
        return Httpresponse("No Get method allowed",status=status.HTTP_400_BAD-REQUEST)
        
