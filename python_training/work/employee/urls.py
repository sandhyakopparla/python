from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.employeePage,name="employeePage"),
]
    
