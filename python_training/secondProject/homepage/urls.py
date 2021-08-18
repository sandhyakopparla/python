from django.urls import path,include
from . import views
urlpatterns = [
    path('/',views.myMainPage,name="myMainPage"),
    path('contact/',views.myContactPage,name="myContactPage"),
    path('gallery/',views.myGallaryPage,name="myGallarypage"),
    
]
