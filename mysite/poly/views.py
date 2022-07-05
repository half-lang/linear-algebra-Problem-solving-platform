from django.shortcuts import render
from django.http import JsonResponse
from linalgpy.latex.parser import matParser, exprParser
from linalgpy.poly import poly
import json,os
from FormulaRecognition import formulaRecognition
dir=os.getcwd().replace('\\','/')

# Create your views here.

def PolySolverPage(request):
    return render(request, 'poly/PolySolverPage.html')

def PolySolver(request):
    js = json.loads(request.body)
    mat = matParser(js['matrix'])
    var = exprParser(js['var'])
    expr = exprParser(js['poly'])
    jsdata = poly.PolySolver(mat, var, expr).dict()
    return JsonResponse(jsdata)


def SchmidtPolySolverPage(request):
    return render(request, 'poly/SchmidtPolySolverPage.html')

def SchmidtPolySolver(request):
    js = json.loads(request.body)
    var = exprParser(js['var'])
    group = list(matParser(js['group']))
    jsdata = poly.SchmidtPolySolver(group, var).dict()
    return JsonResponse(jsdata)

def files(request):
    # 由前端指定的name获取到图片数据
    img = request.FILES.get('img')
    # 获取图片的全文件名
    img_name = img.name
    # 截取文件后缀和文件名
    mobile = os.path.splitext(img_name)[0]
    ext = os.path.splitext(img_name)[1]
    # 重定义文件名
    img_name = f'{mobile}{ext}'
    print(img_name)
    # 从配置文件中载入图片保存路径
    img_path = os.path.join(dir+'/static/img/', img_name)
    # 写入文件
    with open(img_path, 'ab') as fp:
        # 如果上传的图片非常大，就通过chunks()方法分割成多个片段来上传
        for chunk in img.chunks():
            fp.write(chunk)
    prediction, real_label = formulaRecognition(img_name)
    resultdata = ''.join(real_label)
    return render(request,'poly/PolySolverPage.html', {"html_data_name":resultdata})
    # return JsonResponse(jsdata)