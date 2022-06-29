from django.shortcuts import render
from django.http import JsonResponse
from linalgpy.latex.parser import matParser, exprParser
from linalgpy.poly import poly
import json

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