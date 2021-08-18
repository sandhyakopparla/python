from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt 
def productPage(request):
    if(request.method=="POST"):
        getProductName=request.POST.get("productname")
        getDescription=request.POST.get("description")
        getmanufacturingDate=request.POST.get("manufacturingdate")
        getExpiryDate=request.POST.get("expirydate")
        getSellingPrice=request.POST.get("Sellingprice")
        getRetailPrice=request.POST.get("retailprice")
        getWholesalePrice=request.POST.get("wholesaleprice")
        mydict={"productname":getProductName,"description":getDescription,"manufacturingdate":getmanufacturingDate,"expirydate":getExpiryDate,"Sellingprice":getSellingPrice,"retailprice":getRetailPrice,"wholesaleprice":getWholesalePrice}
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return Httpresponse("No Get method allowed") 

# Create your views here.
