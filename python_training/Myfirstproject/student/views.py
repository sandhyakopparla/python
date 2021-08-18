from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myMainPage(request):
    return HttpResponse("hello")
def myUpdatePage(request):
    return HttpResponse("MY update page")

