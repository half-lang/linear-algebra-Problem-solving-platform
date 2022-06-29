from linalgpy.mnmatrix.mnmatrix import mn_matrix
import sympy as sp
from sympy import Expr, simplify


# 行变换

class ele_row_tran_mn(mn_matrix):
    '''
    初等变换：交换m，n行
    '''

    def __init__(self, mat: mn_matrix, m_ind, n_ind) -> None:
        super().__init__()
        self.mat = mat # 内置未作初等变换的矩阵
        self.m_ind = simplify(m_ind)
        self.n_ind = simplify(n_ind)

    def get(self, x: Expr, y: Expr):
        if sp.Eq(x, self.m_ind) == True:
            return self.mat.get(self.n_ind, y)
        elif sp.Eq(x, self.n_ind) == True:
            return self.mat.get(self.m_ind, y)
        else:
            return self.mat.get(x, y)



class ele_row_tran_km(mn_matrix):
    '''
    初等变换：m行乘k
    '''

    def __init__(self, mat: mn_matrix, k, m_ind) -> None:
        super().__init__()
        self.mat = mat # 内置未作初等变换的矩阵
        self.k = simplify(k)
        self.m_ind = simplify(m_ind)


    def get(self, x: Expr, y: Expr):
        if sp.Eq(x, self.m_ind) == True:
            return sp.Mul(self.mat.get(self.m_ind, y), self.k)
        else:
            return self.mat.get(x, y)

class ele_row_tran_kmn(mn_matrix):
    '''
    初等变换：m行乘k，再加到n行
    '''

    def __init__(self, mat: mn_matrix, k, m_ind, n_ind) -> None:
        super().__init__()
        self.mat = mat # 内置未作初等变换的矩阵
        self.k = simplify(k)
        self.m_ind = simplify(m_ind)
        self.n_ind = simplify(n_ind)



    def get(self, x: Expr, y: Expr):
        if sp.Eq(x, self.n_ind) == True:
            return sp.Add(self.mat.get(self.n_ind, y), self.k*self.mat.get(self.m_ind, y))
        else:
            return self.mat.get(x, y)


# 列变换

class ele_col_tran_mn(mn_matrix):
    '''
    初等变换：交换m，n列
    '''

    def __init__(self, mat: mn_matrix, m_ind, n_ind) -> None:
        super().__init__()
        self.mat = mat # 内置未作初等变换的矩阵
        self.m_ind = simplify(m_ind)
        self.n_ind = simplify(n_ind)



    def get(self, x: Expr, y: Expr):
        if sp.Eq(y, self.m_ind) == True:
            return self.mat.get(x, self.n_ind)
        elif sp.Eq(y, self.n_ind) == True:
            return self.mat.get(x, self.m_ind)
        else:
            return self.mat.get(x, y)


class ele_col_tran_km(mn_matrix):
    '''
    初等变换：m列乘k
    '''

    def __init__(self, mat: mn_matrix, k, m_ind) -> None:
        super().__init__()
        self.mat = mat # 内置未作初等变换的矩阵
        self.k = simplify(k)
        self.m_ind = simplify(m_ind)



    def get(self, x: Expr, y: Expr):
        if sp.Eq(y, self.m_ind) == True:
            return sp.Mul(self.mat.get(x, self.m_ind), self.k)
        else:
            return self.mat.get(x, y)

class ele_col_tran_kmn(mn_matrix):
    '''
    初等变换：m列乘k，再加到n列
    '''

    def __init__(self, mat: mn_matrix, k, m_ind, n_ind) -> None:
        super().__init__()
        self.mat = mat # 内置未作初等变换的矩阵
        self.k = simplify(k)
        self.m_ind = simplify(m_ind)
        self.n_ind = simplify(n_ind)


    def get(self, x: Expr, y: Expr):
        if sp.Eq(y, self.n_ind) == True:
            return sp.Add(self.mat.get(x, self.n_ind), self.k*self.mat.get(x, self.m_ind))
        else:
            return self.mat.get(x, y)
