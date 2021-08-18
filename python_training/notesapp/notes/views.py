from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from notes.serializers import NotesSerializer
from notes.models import Notes
from rest_framework.parsers import JSONParser 
from rest_framework import status
@csrf_exempt
def notes_details(request,fetchid):
    try:
        notes=Notes.objects.get(id=fetchid)
        if(request.method=="GET"):
            notes_serializer=NotesSerializer(notes)
            return JsonResponse(notes_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            notes.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            notes_serializer=NotesSerializer(notes,data=mydict)
            if(notes_serializer.is_valid()):
                notes_serializer.save()
                return JsonResponse(notes_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(notes_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Notes.DoesNotExist:
        return HttpResponse("invalid Notes Id",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def notes_list(request):
    if(request.method=="GET"):
        notes=Notes.objects.all()
        notes_serializer=NotesSerializer(notes,many=True)
        return JsonResponse(notes_serializer.data,safe=False)

@csrf_exempt
def notesPage(request):
    if(request.method=="POST"):
       mydict=JSONParser().parse(request)   
       notes_serialize=NotesSerializer(data=mydict)  
       if(notes_serialize.is_valid()):
           notes_serialize.save()
           return JsonResponse(notes_serialize.data,status=status.HTTP_200_OK)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Httpresponse("No Get method allowed",status=status.HTTP_400_BAD-REQUEST)
        


