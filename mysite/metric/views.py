import json
from django.http import JsonResponse
from django.shortcuts import render
from lam.readtext.readtext import readtext
from lam.metric import schmidt

# Create your views here.
'''斯密德正交化求解模块后端'''
def SchmidtVectorSolver(request):
    mat = readtext(json.loads(request.body)['matrix'])
    jsdata = schmidt.SchmidtVectorSolver(mat).dict()
    return JsonResponse(jsdata)

def SchmidtVectorSolverPage(request):
    return render(request, 'metric/SchmidtVectorSolverPage.html')