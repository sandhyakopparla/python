from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.Add,name="Add"),
    path('sub/',views.Sub,name="Sub"),
    path('mul/',views.Mul,name="Mul"),
    path('div/',views.Div,name="Div"),
    


]