from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myMainPage(request):
    return HttpResponse("welome to home page ")
def myContactPage(request):
    return HttpResponse("welcome to my contact page")
def myGallaryPage(request):
    return HttpResponse("welcome to my gallary page") 

