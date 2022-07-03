from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
from initpage.models import User
from django.contrib import messages
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
            messages.error(request,"登录失败")
            print("登录失败")
    return render(request,'log_in.html')

def logon(request):
    if request.method == 'POST':
        print("注册页面")
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        email = request.POST.get('email')
        age = request.POST.get('age')
        print(age)
        sex = request.POST.get('sex')
        telephone=request.POST.get('telephone')
        id=User.objects.all().count()+1
        User.objects.create(id=id,username=username,password=password,email=email,age=age,sex=sex,telephone=telephone)
        print("注册成功")
        messages.error(request, "注册成功")
        return redirect('login')
    return render(request,'log_on.html')