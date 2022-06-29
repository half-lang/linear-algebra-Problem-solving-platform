import __init__
import sympy as sp
from linalgpy.quad.quadratic import QuadSolver, HurwitzSolver

import logging


def test1():
    mat = sp.Matrix([
    [0,1,1,0],
    [1,0,-3,0],
    [1,-3,0,0],
    [0,0,0,3]
    ])
    solver = QuadSolver(mat)
    logging.debug(solver.result)
    logging.debug(solver.trans)
    logging.debug(solver.mark)

def test2():
    mat = sp.Matrix([
    [0,1,1,0],
    [1,0,-3,0],
    [1,-3,0,0],
    [0,0,0,3]
    ])
    solver = QuadSolver(mat)
    logging.debug(solver.dict())

def test3():
    mat = sp.Matrix([[1,2,3],[4,3,3]])
    logging.debug(mat.minor_submatrix(-1, -1))
    logging.debug(mat)

def test4():
    ls = []
    ls.insert(0,1)
    print(ls)

def test5():
    mat = sp.Matrix([[1,3,3],[3,3,3],[3,3,3]])
    sl = HurwitzSolver(mat)
    dc = sl.dict()
    logging.debug(dc)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test5()