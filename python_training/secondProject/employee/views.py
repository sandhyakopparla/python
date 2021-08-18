from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myAddPage(request):
    return HttpResponse("welome to my employee add age ")
def myEditPage(request):
    return HttpResponse("welcome to my employee edit page")
def myDeletePage(request):
    return HttpResponse("welcome to my employee delete page")
def mySearchPage(request):
    return HttpResponse("welcome to my employee search page") 

# Create your views here.
