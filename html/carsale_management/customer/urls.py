from django.urls import path,include
from . import views
urlpatterns =[
    path('add/',views.customerPage,name="customerPage"),
    path('viewall/',views.customer_list,name="customer_list"),
    path('search/',views.searchapi,name='searchapi'),
    path('updateapi/',views.update_api,name='update_api'),
    path('viewcustomer/<fetchid>',views.customer_details,name='customer_details'),
    #html
    path('register/',views.customerregister_view,name="customerregister_name"),
    path('customerview/',views.viewall,name="viewall"),
    path('searchview/',views.search_view,name='search_view'),
    path('updatescreen/',views.update_view,name='update_view'),
    path('updatedata/',views.update_data_read,name='update_data_read'),
    path('deletedata/',views.delete_data_read,name='delete_data_read'),
    path('deletescreen/',views.delete_view,name='delete_view'),
    path('delete_api/',views.delete_api,name='delete_api'),
] 