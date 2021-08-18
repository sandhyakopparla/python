from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.employeePage,name="employeePage"),
    path('viewall/',views.employee_list,name='employee_list'),
    path('viewemployee/<fetchid>',views.employee_details,name='employee_details')
]