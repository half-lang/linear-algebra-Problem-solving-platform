import sympy as sp
from sympy.core.numbers import Rational
from linalgpy.determinant import course
from linalgpy.printing import latextext

def formtest() -> str:
    a = sp.symbols('a')
    b = sp.symbols('b')
    c = sp.symbols('c')
    mat = sp.Matrix([
        [1,2,3,a],
        [0,3,c,2],
        [9,b,Rational(3,7),3],
        [7,8,2,1],
    ])
    co = course.det_course(mat)
    text = ''
    for x in co['expand']:
        text = text + '$' + latextext.latex(x, mat_delim = '|') + '$' + r'<br>'
    for x in co['figure']:
        text = text + '$' + latextext.latex(x) + '$' + r'<br>'
    return text