from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt 
def companyPage(request):
    if(request.method=="POST"):
        getcompanyName=request.POST.get("companyname")
        getaddress=request.POST.get("address")
        getwebsite=request.POST.get("website")
        getphonenumber=request.POST.get("phonenumber")
        getemail=request.POST.get("email")
        getdirector=request.POST.get("director")
        mydict={"companyname":getcompanyName,"address":getaddress,"website":getwebsite,"phonenumber":getphonenumber,"email":getemail,"director":getdirector}
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return Httpresponse("No Get method allowed") 

# Create your views here.


# Create your views here.
