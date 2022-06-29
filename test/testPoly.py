from cgi import test
import __init__
import sympy as sp
from sympy.abc import n, x
from linalgpy.poly.poly import PolySolver, SchmidtPolySolver
from sympy.parsing.latex import parse_latex
import logging

def test1():
    expr: sp.Poly = sp.poly(3*n*x + 2*x**3, x)
    logging.debug(expr.all_coeffs())
    rs = expr.args[0].subs(x, sp.Matrix([[1,1],[1,1]]))
    logging.debug(rs)

def test2():
    x = sp.MatrixSymbol('x', 2, 2)
    expr = x**2 + 3*n*x
    expr = expr.subs(x, sp.Matrix([[1,1],[1,1]]))
    logging.debug(type(expr))
    logging.debug(expr.as_explicit())

def test3():
    mat = sp.Matrix([[1,2],[3,4]])
    var = x
    poly = x**3 + x + 1
    sl = PolySolver(mat, var, poly)
    js = sl.toDict()
    print(js['matPoly'])
    print(js['subPoly'])

def test4():
    mat = sp.Matrix([[1,2],[3,4]])
    a = parse_latex("x")
    b = sp.simplify(parse_latex("x+x^2+1+x"))
    p = sp.Poly(b, a)
    print(p)

def test5():
    group = [1, x, x**2]
    var = x
    sl = SchmidtPolySolver(group, var)
    dc = sl.dict()
    logging.debug(dc['coef'])
    logging.debug(sl.coef[0,:])
    logging.debug(list(sl.coef[0,:]))

    

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # a = sp.integrate(x**2*(x-sp.Rational(1,2)), (x, 0, 1))
    # print(a)
    test5()