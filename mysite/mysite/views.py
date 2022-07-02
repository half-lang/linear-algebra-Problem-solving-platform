from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
from initpage.models import User

def home_page(request):
    return render(request, 'HOME.html')

def login(request):
    if request.method == 'POST':
        print("进入页面")
        username = request.POST.get('username')
        password = request.POST.get('password')
        corr_username = User.objects.filter(username=username).first()
        print(corr_username)
        print("获取到信息")
        if username == corr_username.username and password == corr_username.password:
            print("登录成功")
            return redirect("home")
        else:
            print("登录失败")
    return render(request,'log_in.html')

def logon(request):
    return render(request,'log_on.html')