from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from customer.serializers import customerSerializer
from customer.models import Customer
from rest_framework.parsers import JSONParser 
from rest_framework import status
import requests
@csrf_exempt
def delete_data_read(request):
    getId=request.POST.get("newid")
    ApiLink="http://localhost:8000/customer/viewcustomer/"+ getId 
    requests.delete(ApiLink)
    return HttpResponse("data deleted successfully")
@csrf_exempt
def delete_api(request):
    try:
        getmobile_no=request.POST.get("mobile_no")
        getMobile=Customer.objects.filter(mobile_no=getmobile_no)
        customer_serializer=customerSerializer(getMobile,many=True)
        return render(request,"delete.html",{"data":customer_serializer.data})
    except:
        return HttpResponse("invalid building number")
@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")
    getName=request.POST.get("newname")
    getAddress=request.POST.get("newaddress")
    getmobile_no=request.POST.get("newmobilenumber")
    getcarmodel=request.POST.get("newcarmodel")
    getcarmodel_year=request.POST.get("newcarmodelyear")
    getpurchasedate=request.POST.get("newpurchaseddate")
    getusername=request.POST.get("newusername")
    getpassword=request.POST.get("newpassword") 
    mydata={"name":getName,"address":getAddress,"mobile_no":getmobile_no,"car_model":getcarmodel,"carmodel_year":getcarmodel_year,"purchased_date":getpurchasedate,"username":getusername,"password":getpassword}
    jsondata=json.dumps(mydata)
    ApiLink="http://localhost:8000/customer/viewcustomer/"+ getId
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("data updated successfully")
@csrf_exempt 
def update_api(request):
    try:
        getmobile_no=request.POST.get("mobile_no")
        getMobile=Customer.objects.filter(mobile_no=getmobile_no)
        customer_serializer=customerSerializer(getMobile,many=True)
        return render(request,"update.html",{"data":customer_serializer.data})

    except:
        return HttpResponse("invalid Mobile number")
@csrf_exempt
def searchapi(request):
    try:
        getmobile_no=request.POST.get("mobile_no")
        getMobile=Customer.objects.filter(mobile_no=getmobile_no)
        customer_serializer=customerSerializer(getMobile,many=True)
        return render(request,"search.html",{"data":customer_serializer.data})
    except:
        return HttpResponse("invalid mobile number")
@csrf_exempt
def customerPage(request):
    if(request.method=="POST"):
    #    mydict=JSONParser().parse(request)   
       customer_serialize=customerSerializer(data=request.POST)  
       if(customer_serialize.is_valid()):
           customer_serialize.save()
           return redirect(viewall)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
def customer_list(request):
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