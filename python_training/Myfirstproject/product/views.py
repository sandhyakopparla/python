from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myAddPage(request):
    return HttpResponse("product is added")
def myUpdatePage(request):
    return HttpResponse("product is updated")
def myDeletePage(request):
    return HttpResponse("product is deleted")
def mySearchPage(request):
    return HttpResponse("product is search")


# Create your views here.
