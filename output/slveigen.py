from lam.eigen.eigenvalue import *
import json
from lam.readtext.readtext import readtext
import sympy as sp
import sympy.core.numbers as nu
import numpy as np
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj,sp.core.numbers.Integer):
            return str(obj)
        else:
            return str(obj)
def slveigengetcharpoly(a:str):#特征多项式
    eigenSolver = EigenSolver(readtext(a))
    p = eigenSolver.getCharpoly()
    p=sp.latex(p)
    print(p)
    json_str = json.dumps(p)
    return json_str
def slveigenvalue(a:str):#特征值
    eigenSolver = EigenSolver(readtext(a))
    p = eigenSolver.getEigenvalues()
    p = sp.latex(p)
    json_str = json.dumps(p)
    return json_str
def slveigenvectors(a:str):#特征向量
    eigenSolver = EigenSolver(readtext(a))
    eigenvectors = eigenSolver.getEigenvectors()
    eigenvectors_0 = []
    for i in range(len(eigenvectors)):
        m = (sp.latex(eigenvectors[i][0]), sp.latex(eigenvectors[i][1]), sp.latex(eigenvectors[i][2][0]))
        eigenvectors_0.append(m)
    eigenvectors=eigenvectors_0
    json_str = json.dumps(eigenvectors)
    return json_str
def slveigenCourse(a:str):#（特征值求解过程）
    eigenSolver=EigenSolver(readtext(a))
    p=eigenSolver.get_course()
    matrix=p['matrix']
    eigenvectors=p['eigenvectors']
    charpoly=p['charpoly']
    matrix=sp.latex(matrix)
    charpoly=sp.latex(charpoly)
    eigenvectors_0=[]
    for i in range(len(eigenvectors)):
        m = (sp.latex(eigenvectors[i][0]),sp.latex(eigenvectors[i][1]),sp.latex(eigenvectors[i][2][0]))
        eigenvectors_0.append(m)
    p['matrix']=matrix
    p['eigenvetors']=eigenvectors_0
    p['charpoly']=charpoly
    json_str = json.dumps(p,cls=MyEncoder,indent=4)
    return json_str

