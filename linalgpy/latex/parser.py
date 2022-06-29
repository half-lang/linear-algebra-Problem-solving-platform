from linalgpy.latex.latextrans import *
from sympy import MutableDenseMatrix, Expr
from sympy.parsing.latex import parse_latex

def matParser(x: str) -> MutableDenseMatrix:
    return standard_transformation(latextrans(x))

def exprParser(x: str) -> Expr:
    return parse_latex(x)
