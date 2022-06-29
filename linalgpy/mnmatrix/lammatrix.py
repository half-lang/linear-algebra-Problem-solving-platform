import sympy as sp
from sympy import S, Function, simplify
from linalgpy.mnmatrix.mnmatrix import mn_matrix

class id_func(Function):
    '''
    单位矩阵的内置函数
    '''
    @classmethod
    def eval(cls, x, y, m, n):
        if simplify(sp.Eq(x, y)) == True:
            return S.One
        elif simplify(sp.Eq(x, y)) == False:
            return S.Zero

class id_matrix(mn_matrix):
    '''
    定义单位矩阵
    '''
    def __init__(self) -> None:
        self.init_symbol()
        self.init_func(id_func)

class tridiagonal_func(Function):
    '''
    三对角矩阵的内置函数
    '''

    @classmethod
    def eval(cls, x, y, m, n, diag, diag2nd):
        if simplify(sp.Eq(x, y)) == True:
            return diag
        elif simplify(sp.Eq(sp.Abs(x-y), 1)) == True:
            return diag2nd
        elif simplify(sp.Gt(sp.Abs(x-y), 1)) == True:
            return S.Zero

class tridiagonal_matrix(mn_matrix):
    '''
    三对角矩阵的内置函数
    '''

    def __init__(self, diag, diag2nd) -> None:
        self.diag = simplify(diag)
        self.diag2nd = simplify(diag2nd)
        self.init_symbol()
        self.init_func()
    
    def init_func(self):
        self.func: Function = tridiagonal_func(self.x, self.y, self.m, self.n, self.diag, self.diag2nd)

class circ_func(Function):
    '''
    循环矩阵的内置函数
    '''
    @classmethod
    def eval(cls, x, y, m, n):
        diagN = (y - x)
        flag = (y - x).subs(n, 100)
        # s是对角线的序数，以主对角线为第0条对角线，上三角斜线依次为1,...,n-1，
        # 下三角-1,...,-n+1，由于1-n无法判断正负,必须先假定n为一个较大的数，注意这里refine函数也是不能用的
        if flag.is_nonnegative == True: # 如果diagN大于0
            return diagN + 1
        elif flag.is_negative == True:
            return n + 1 + diagN

class circ_matrix(mn_matrix):
    '''
    定义循环矩阵
    '''
    def __init__(self) -> None:
        self.init_symbol()
        self.init_func(circ_func)



if __name__ == "__main__":
    id = id_matrix()
    n = id.n
    res = simplify(sp.Mod(n+2,n))
    res2 = (n+1) / n
    print(res, res2)