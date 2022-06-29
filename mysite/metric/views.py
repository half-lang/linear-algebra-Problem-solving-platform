import json
from django.http import JsonResponse
from django.shortcuts import render
from linalgpy.latex.parser import matParser
from linalgpy.metric import schmidt

# Create your views here.
'''斯密德正交化求解模块后端'''
def SchmidtVectorSolver(request):
    mat = matParser(json.loads(request.body)['matrix'])
    jsdata = schmidt.SchmidtVectorSolver(mat).dict()
    return JsonResponse(jsdata)

def SchmidtVectorSolverPage(request):
    return render(request, 'metric/SchmidtVectorSolverPage.html')