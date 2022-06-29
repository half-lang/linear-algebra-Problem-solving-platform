from linalgpy.determinant.lammatrix import *
from sympy.abc import x,y,z
from sympy import refine, Q, Symbol
from linalgpy.determinant.mnmatrix import scalar_mul

def test1():
    id = id_matrix()
    kid = scalar_mul(Symbol('c'),id)
    a = kid.get(kid.n,kid.n)
    print(a)

def test2():
    tri = tridiagonal_matrix(1,2)
    ktri = scalar_mul(3, tri)
    res = ktri.get(tri.n,tri.n-1)
    print(res)

def test3():
    circ = circ_matrix()
    n = circ.n
    a = circ.get(n-1,2)
    print(a)

def test4():
    flag = refine(x > 3, Q.infinite(x))
    print(flag)

if __name__ == "__main__":
    test3()