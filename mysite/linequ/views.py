import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from linalgpy.latex.parser import matParser, exprParser
from linalgpy.linequ import gausslimination, linequsolver, lambdalinequ, inverse

# Create your views here.

def GESolver(request):
    mat = matParser(json.loads(request.body)['matrix'])
    jsdata = gausslimination.GESolver(mat).dict()
    return JsonResponse(jsdata)

@ensure_csrf_cookie
def GESolverPage(request):
    return render(request, 'linequ/GESolverPage.html')


def LinequSolver(request):
    mat = json.loads(request.body)['matrix']
    mat = matParser(mat)
    jsdata = linequsolver.LinequSolver(mat[:, :-1], mat[:, -1]).dict()
    return JsonResponse(jsdata)

@ensure_csrf_cookie
def LinequSolverPage(request):
    return render(request, 'linequ/LinequSolverPage.html')


def InverseSolver(request):
    mat = json.loads(request.body)['matrix']
    mat = matParser(mat)
    jsdata = inverse.InverseSolver(mat).dict()
    return JsonResponse(jsdata)

@ensure_csrf_cookie
def InverseSolverPage(request):
    return render(request, 'linequ/InverseSolverPage.html')


def LambdaLinSolver(request):
    mat = matParser(json.loads(request.body)['matrix'])
    a = exprParser(json.loads(request.body)['lambda'])
    jsdata = lambdalinequ.LambdaLinSolver(mat, a).dict()
    return JsonResponse(jsdata)

@ensure_csrf_cookie
def LambdaLinSolverPage(request):
    return render(request, 'linequ/LambdaLinSolverPage.html')