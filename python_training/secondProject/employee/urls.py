from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.myAddPage,name="myAddPage"),
    path('edit/',views.myEditPage,name="myEditpage"),
    path('delete/',views.myDeletePage,name="myDeletepage"),
    path('search/',views.mySearchPage,name="mySearchpage"),
]
