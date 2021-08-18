from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.myAddPage,name='myMainPage'),
    path('update/',views.myUpdatePage,name='myUpdatePage'),
    path('delete/',views.myDeletePage,name='myDeletePage'),
    path('search/',views.mySearchPage,name='mySearchPage'),
]
