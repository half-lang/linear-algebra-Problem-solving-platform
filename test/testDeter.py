import __init__
import sympy as sp
from linalgpy.determinant.determinant import DeterminantSolver
from sympy.abc import a, b, c

def test1():
    mat = sp.Matrix([
        [1,1,1,3,4],
        [a,2,2,3,2],
        [4,1,a,-1,3],
        [1,a,3,2,5],
        [1,1,2,a,5],
    ])
    solver = DeterminantSolver(mat)
    dic = solver.dict()
    print(dic['coef'])
    print(dic['operater'])
    print(dic['cofactor'])
    print(mat.det())
    print(solver.sum)
    print(dic['result_operater'])
    print(dic['result'])

if __name__ == "__main__":
    test1()