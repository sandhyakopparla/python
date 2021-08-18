from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myAddPage(request):
    return HttpResponse("welome to my  company add page ")
def myEditPage(request):
    return HttpResponse("welcome to my company edit page")
def myDeletePage(request):
    return HttpResponse("welcome to my company delete page")
def mySearchPage(request):
    return HttpResponse("welcome to my company search page") 

# Create your views here.
