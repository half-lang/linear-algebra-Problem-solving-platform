from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
from django.shortcuts import render, HttpResponse,redirect,reverse
from .models import User
import json


def logout(response):
    return HttpResponse('退出')

def index(request):
    return redirect('')
