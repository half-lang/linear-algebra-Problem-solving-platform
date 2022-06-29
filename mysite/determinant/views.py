from django.shortcuts import render
from django.http import JsonResponse
from linalgpy.determinant import determinant
from linalgpy.latex.parser import matParser
import json

import logging
logging.basicConfig(level=logging.WARN, filename='mylog.txt', filemode='w')
# Create your views here.

def DeterminantSolver(request):
    mat = matParser(json.loads(request.body)['matrix'])
    jsdata = determinant.DeterminantSolver(mat).dict()
    return JsonResponse(jsdata)

def DeterminantSolverPage(request):
    return render(request, 'determinant/DeterminantSolverPage.html')


def GaussDeterminantSolver(request):
    mat = matParser(json.loads(request.body)['matrix'])
    jsdata = determinant.GausseDeterminantSolver(mat).dict()
    return JsonResponse(jsdata)

def GaussDeterminantSolverPage(request):
    return render(request, 'determinant/GaussDeterminantSolverPage.html')