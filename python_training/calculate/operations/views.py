from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def Add(request):
    if(request.method == "POST"):
        getNum1=int(request.POST.get("num1"))
        getNum2=int(request.POST.get("num2"))
        result=getNum1+getNum2  
        mydict={"num1":getNum1,"num2":getNum2,"operation":"addition","result":result}
        resulttodisp=json.dumps(mydict)
        return HttpResponse(resulttodisp)
@csrf_exempt
def Sub(request):
    if(request.method == "POST"):
        getNum1=int(request.POST.get("num1"))
        getNum2=int(request.POST.get("num2"))
        result1=getNum1-getNum2  
        mydict1={"num1":getNum1,"num2":getNum2,"operation":"substraction","result1":result1}
        resulttodisp1=json.dumps(mydict1)
        return HttpResponse(resulttodisp1)
@csrf_exempt
def Mul(request):
    if(request.method == "POST"):
        getNum1=int(request.POST.get("num1"))
        getNum2=int(request.POST.get("num2"))
        result2=getNum1*getNum2  
        mydict2={"num1":getNum1,"num2":getNum2,"operation":"multiply","result2":result2}
        resulttodisp2=json.dumps(mydict2)
        return HttpResponse(resulttodisp2)
@csrf_exempt
def Div(request):
    if(request.method == "POST"):
        getNum1=int(request.POST.get("num1"))
        getNum2=int(request.POST.get("num2"))
        result=getNum1/getNum2  
        mydict={"num1":getNum1,"num2":getNum2,"operation":"addition","result3":result3}
        resulttodisp3=json.dumps(mydict)
        return HttpResponse(resulttodisp3)

# @csrf_exempt
# def studentcalculate(request):
#     if(request.method == "POST"):
#         result=json.dumps(request.POST)
#         result1=json.dumps(request.POST)
#         result2=json.dumps(request.POST)
#         result3=json.dumps(request.POST)
#         return HttpResponse(result)
#     else:
#         return HttpResponse("No GET mathod allowed")

# # Create your views here.
