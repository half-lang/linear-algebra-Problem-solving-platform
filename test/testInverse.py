import __init__
import sympy as sp
from sympy.matrices.dense import Matrix
from linalgpy.linequ.inverse import InverseSolver

import logging
logging.basicConfig(level=logging.DEBUG)

def testIsSingular():
    a = sp.symbols('a')
    mat = sp.diag(*[1 for i in range(3)])
    mat = Matrix.hstack(mat, mat)
    print(a*0, bool(a*0), mat)
    return

def testInv():
    mat = [
        [0, 1, 1],
        [1, 2, 1],
        [1, 1, 2],
    ]
    mat = sp.Matrix(mat)
    solver = InverseSolver(mat)
    # logging.debug(solver.course)
    # logging.debug(solver.inv @ mat)
    logging.debug(solver.dict())

if __name__ == "__main__":
    testInv()