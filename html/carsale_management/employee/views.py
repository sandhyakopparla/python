from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from employee.serializers import employeeSerializer
from employee.models import Employee
from rest_framework.parsers import JSONParser 
from rest_framework import status
import requests
@csrf_exempt
def delete_data_read(request):
    getId=request.POST.get("newid")
    ApiLink="http://localhost:8000/employee/viewemployee/"+ getId 
    requests.delete(ApiLink)
    return HttpResponse("data deleted successfully")
@csrf_exempt
def delete_api(request):
    try:
        getempname=request.POST.get("name")
        getName=Employee.objects.filter(name=getempname)
        employee_serializer=employeeSerializer(getName,many=True)
        return render(request,"delete.html",{"data":employee_serializer.data})
    except:
        return HttpResponse("invalid building number")
@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")
    getempcode=request.POST.get("newempcode")
    getName=request.POST.get("newname")
    getsalary=request.POST.get("newsalary")
    getdateoj=request.POST.get("newdate_of_joining")
    getDesignation=request.POST.get("newdesignation")
    getusername=request.POST.get("newusername")
    getpassword=request.POST.get("newpassword")
   
    mydata={"empcode":getempcode,"name":getName,"salary":getsalary,"date_of_joining":getdateoj,"designation":getDesignation,"username":getusername,"username":getusername,"password":getpassword}
    jsondata=json.dumps(mydata)
    ApiLink="http://localhost:8000/employee/viewemployee/"+ getId
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("data updated successfully")
@csrf_exempt 
def update_api(request):
    try:
        getempname=request.POST.get("name")
        getName=Employee.objects.filter(name=getempname)
        employee_serializer=employeeSerializer(getName,many=True)
        return render(request,"update.html",{"data":employee_serializer.data})

    except:
        return HttpResponse("invalid Employee name")
@csrf_exempt
def searchapi(request):
    try:
        getempname=request.POST.get("name")
        getName=Employee.objects.filter(name=getempname)
        employee_serializer=employeeSerializer(getName,many=True)
        return render(request,"search.html",{"data":employee_serializer.data})
    except:
        return HttpResponse("invalid mobile number")
@csrf_exempt
def EmployeePage(request):
    if(request.method=="POST"):
    #    mydict=JSONParser().parse(request)   
       employee_serialize=employeeSerializer(data=request.POST)  
       if(employee_serialize.is_valid()):
           employee_serialize.save()
           return redirect(viewall)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
def employee_list(request):
    if(request.method=="GET"):
        customer=Customer.objects.all()
        customer_serialize=customerSerializer(customer,many=True)
        return JsonResponse(customer_serialize.data,safe=False)
@csrf_exempt
def customer_details(request,fetchid):
    try:
        customer=Customer.objects.get(id=fetchid)
        if(request.method=="GET"):
            customer_serializer=customerSerializer(customer)
            return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            customer.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            customer_serializer=customerSerializer(customer,data=mydict)
            if(customer_serializer.is_valid()):
                customer_serializer.save()
                return JsonResponse(customer_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(customer_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Customer.DoesNotExist:
        return HttpResponse("invalid customer id",status=status.HTTP_404_NOT_FOUND)
def customerregister_view(request):
    return render(request,'register.html')
def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/customer/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})
def search_view(request):
    return render(request,'search.html')
def update_view(request):
    return render(request,'update.html')
def delete_view(request):
    return render(request,'delete.html')