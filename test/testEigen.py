from cgi import test
import __init__
from linalgpy.eigen.eigen import *
from linalgpy.eigen.diagnoalize import *
import sympy as sp
import logging

mat = sp.Matrix([
    [1,2,2],
    [2,1,2],
    [2,2,1]
])

def test1():
    sl = EigenValueSolver(mat)
    dc = sl.dict()
    # logging.debug(sl.charpoly)
    # logging.debug(list(sl.result.items()))
    logging.debug(dc['result'])
    logging.debug(dc['charpoly'])
    logging.debug(dc['lambda_mat'])

def test2():
    sl = EigenVectorSolver(mat)
    dc = sl.dict()
    # logging.debug(sl.result)
    logging.debug(dc['result'])
    # logging.debug(dc['equ_mat'])
    # logging.debug(dc['EVAS'])

def test3():
    sl = DiagSymmetricSolver(mat)
    dc = sl.dict()
    print(dc)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    test3()