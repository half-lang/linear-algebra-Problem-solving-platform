from linalgpy.mnmatrix.eletran import *
from linalgpy.mnmatrix.lammatrix import *
from linalgpy.mnmatrix.mnmatrix import add_matrix, scalar_mul_matrix

def test1():
    mat: mn_matrix = circ_matrix()
    print(mat.get(mat.n, mat.n))
    mat = ele_col_tran_kmn(mat, 2, 1, mat.n)
    print(mat.get(mat.n, mat.n))

def test2():
    ma: mn_matrix = circ_matrix()
    mb: mn_matrix = circ_matrix()
    mc = add_matrix(ma, mb)
    print(mc.get(3,2))

def test3():
    mat: mn_matrix = circ_matrix()
    mat = scalar_mul_matrix(mat, 3)
    print(mat.get(3,2))


if __name__ == "__main__":
    test3()