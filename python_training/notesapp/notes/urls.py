from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.notesPage,name="notesPage"),
    path('viewall/',views.notes_list,name='notes_list'),
    path('viewnotes/<fetchid>',views.notes_details,name='notes_details'),
]