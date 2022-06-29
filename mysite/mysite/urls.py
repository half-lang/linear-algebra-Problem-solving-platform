"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',  views.home_page),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('demo/', include('demo.urls')),
    path('eigen/',include('eigen.urls')),
    path('determinant/',include('determinant.urls')),
    path('quad/',include('quad.urls')),
    path('linequ/',include('linequ.urls')),
    path('metric/',include('metric.urls')),
    path('linspace/',include('linspace.urls')),
    path('poly/',include('poly.urls')),
]

