from django.urls import path
from . import views

urlpatterns =[
    path('logon/',views.logon,name='logon'),
    path('logout/',views.logout,name='logout'),
]