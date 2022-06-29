import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from linalgpy.linspace import MLIG, lincombination, linspace
from linalgpy.latex.parser import matParser

# Create your views here.
def MLIGSolver(request):
    mat = matParser(json.loads(request.body)['matrix'])
    ls = []
    for i in range(mat.shape[0]):
        ls.append(mat[i, :])
    jsdata = MLIG.MLIGSolver(ls).dict()
    return JsonResponse(jsdata)

@ensure_csrf_cookie
def MLIGSolverPage(request):
    return render(request, 'linspace/MLIGSolverPage.html')


def LincombinationSolver(request):
    js = json.loads(request.body)
    mat = matParser(js['matrix'])
    vec = matParser(js['vector'])
    jsdata = lincombination.LincombinationSolver(mat, vec).dict()
    return JsonResponse(jsdata)

@ensure_csrf_cookie
def LincombinationSolverPage(request):
    return render(request, 'linspace/LincombinationSolverPage.html')


def LinDependenceSolver(request):
    mat = matParser(json.loads(request.body)['matrix'])
    jsdata = linspace.LinDependenceSolver(mat).dict()
    return JsonResponse(jsdata)

@ensure_csrf_cookie
def LinDependenceSolverPage(request):
    return render(request, 'linspace/LinDependenceSolverPage.html')


def BasisTransSolver(request):
    js = json.loads(request.body)
    mat = matParser(js['matrix'])
    ma = matParser(js['ma'])
    mb = matParser(js['mb'])
    jsdata = linspace.BasisTransSolver(mat, ma, mb).dict()
    return JsonResponse(jsdata)

@ensure_csrf_cookie
def BasisTransSolverPage(request):
    return render(request, 'linspace/BasisTransSolverPage.html')