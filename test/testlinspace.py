import __init__
import sympy as sp
from linalgpy.linspace.MLIG import MLIGSolver
from linalgpy.linspace.lincombination import LincombinationSolver
from linalgpy.linspace.linspace import LinDependenceSolver, BasisTransSolver

ma = sp.Matrix([[1,2,3,-1], [3,2,1,-1], [2,3,1,1], [2,2,2,-1], [5,5,2,0]])
mb = sp.Matrix([[1,2,3], [3,2,1], [0,0,0]])
vec = sp.Matrix([[-1],[-1],[0]])

def test1():
    for i in range(len(ma)):
        ma[i] = sp.Matrix(ma[i])
    solver = MLIGSolver(ma)
    print(solver.dict())

def test2():
    rs = sp.linsolve(ma)
    print(rs.is_empty)

def test3():
    sl = LincombinationSolver(mb, vec)
    dc = sl.dict()
    print(dc['solveset'])

def test4():
    sl = LinDependenceSolver(ma)
    dc = sl.dict()
    print(dc['result'])
    print(dc['GES'])

def test5():
    ma = sp.Matrix([[-1,1,1], [1,0,1], [0,1,1]])
    mb = sp.Matrix([[1,0,0], [0,1,0], [0,0,1]])
    mat = sp.Matrix([[1,0,1],[1,1,0],[-1,2,1]])
    sl = BasisTransSolver(mat, ma, mb)
    dc = sl.dict()
    print(dc)

if __name__ == "__main__":
    test5()
