from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt 
def employeePage(request):
    if(request.method=="POST"):
        getName=request.POST.get("name")
        getId=request.POST.get("id")
        getDesignation=request.POST.get("designation")
        getSalary=request.POST.get("salary")
        getPhno=request.POST.get("phonenumber")
        mydict={"name":getName,"id":getId,"designation":getDesignation,"salary":getSalary,"phonenumber":getPhno}
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return Httpresponse("No Get method allowed")  