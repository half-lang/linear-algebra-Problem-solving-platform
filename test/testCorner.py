import sympy as sp
from linalgpy.mnmatrix.cornermatrix import *
from sympy.abc import n
from linalgpy.mnmatrix.eletran import *

tl = sp.Matrix([[1,2], [2,3]])
tr = sp.Matrix([[1,n], [2,n]])
bl = sp.Matrix([[n,2], [n,3]])
br = sp.Matrix([[n,n], [n,n]])


def test1():
    mat = corner_matrix(tl, tr, bl, br)
    print(mat.get(mat.n-1, 2))

def test2():
    mat = corner_matrix(tl, tr, bl, br)
    mat = ele_col_tran_km(mat, 3, mat.n)
    print(mat.get(mat.n, mat.n - 1))

if __name__ == "__main__":
    test2()
