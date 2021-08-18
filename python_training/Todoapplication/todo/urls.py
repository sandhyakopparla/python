from django.urls import path,include
from . import views
urlpatterns =[
    path('add/',views.todoPage,name="todoPage"),
    path('viewall/',views.todo_list,name='todo_list'),
]