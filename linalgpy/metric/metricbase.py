import sympy as sp
import logging
from sympy import MutableDenseMatrix
from sympy.abc import x
from sympy.core import Expr, Number
from sympy.core.function import Lambda


def vector_inner(a: MutableDenseMatrix, b: MutableDenseMatrix) -> MutableDenseMatrix:
    # 封装内积
    return a.dot(b)

def poly_inner(a: Expr, b: Expr) -> Number:
    # 多项式内积，只支持sympy.abc.x为自变量
    return sp.integrate(a*b, (x, 0, 1))

def normalize(vec: MutableDenseMatrix):
    # 单位化向量
    return sp.Mul(sp.Pow(vec.norm(), -1), vec)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    a = sp.Matrix([1,2,3])
    b = sp.Matrix([5,32,4])
    logging.debug(vector_inner(a, b))