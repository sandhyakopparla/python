from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from todo.serializers import TodoSerializer
from todo.models import Todo
from rest_framework.parsers import JSONParser 
from rest_framework import status
# Create your views here.
@csrf_exempt
def todoPage(request):
    if(request.method=="POST"):
       mydict=JSONParser().parse(request)   
       todo_serialize=TodoSerializer(data=mydict)  
       if(todo_serialize.is_valid()):
           todo_serialize.save()
           return JsonResponse(todo_serialize.data,status=status.HTTP_200_OK)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Httpresponse("No Get method allowed",status=status.HTTP_400_BAD-REQUEST) 
@csrf_exempt
def todo_list(request):
    if(request.method=="GET"):
        todo=Todo.objects.all()
        todo_serializer=TodoSerializer(todo,many=True)
        return JsonResponse(todo_serializer.data,safe=False)
@csrf_exempt
def todo_details(request,fetchid):
    if(request.method=="GET"):
        todo_serializer=TodoSerializer(todo)
        return JsonResponse(todo_serializer.data,safe=False,status=status.HTTP_200_OK) 
        