import __init__
import sympy as sp
from sympy.abc import m, n, x, t
from sympy.core.function import Lambda
from lam.metric.schmidt import Schmidt_orther
from lam.metric.metricbase import vector_inner, poly_inner

import logging
logging.basicConfig(level=logging.WARN)

def test_vec_orther():
    data = [
        [1,1,0,0],
        [1,0,1,0],
        [-1,0,0,1],
        [1,-1,-1,1],
    ]
    for i in range(len(data)):
        data[i] = sp.Matrix(data[i])
    sovler = Schmidt_orther(data, vector_inner)
    logging.debug(sovler.get_course())

def test_poly_orther():
    data = [1, x, x**2]
    # data = [1, m*x, n*x**2]
    solver = Schmidt_orther(data, poly_inner)
    logging.debug(solver.get_course())

def test_func():
    f: Lambda = Lambda(x, x**2)
    g: Lambda = Lambda(x, x)
    fe, ge = f.expr, g.expr
    logging.debug(fe+ge+1)

if __name__ == "__main__":
    
    # a = sp.Mul(sp.Pow(n/2, -1), m/2)
    # logging.debug(a)
    test_poly_orther()
