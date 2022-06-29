import json
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest

#尚未打包安装，请先将工具包加入环境变量，已改为相对路径，已在init文件处引入
# import sys
# from pathlib import Path
# lampy_dir = Path(__file__).resolve().parent.parent.parent
# sys.path.append(str(lampy_dir))


# Create your views here.

def demo(request):
    return render(request, 'demo/demoPage.html')

def answer(request):
    return render(request,'demo/answerPage.html')


def gaussElim(request):
    return render(request, 'demo/GEMPage.html')

def testPage(request):
    return render(request, 'demo/testPage.html')

def csrf_test_func(request):
    data = json.loads(request.body)
    return JsonResponse(data)

def csrf_page(request: HttpRequest):
    return render(request, 'demo/csrfTest.html')

def testSolver(request: HttpRequest):
    data = json.loads(request.body)['matrix']
    data = {'matrix': data}
    s = data['matrix']
    print(s)
    print(data)
    return JsonResponse(data)