import sympy as sp
from sympy import Function, simplify, Expr, Symbol



class mn_matrix:
    '''
    定义m*n大小的矩阵
    '''

    def __init__(self) -> None:
        self.init_symbol()
        self.init_func(Function('matrix'))

    def init_func(self, f):
        self.func: Function = f(self.x, self.y, self.m, self.n)

    def init_symbol(self):
        self.m = Symbol('m', positive=True, integer=True)
        self.n = Symbol('n', positive=True, integer=True)
        self.x = Symbol('x', positive=True, integer=True)
        self.y = Symbol('y', positive=True, integer=True)

    def get_symbol(self):
        return (self.x, self.y, self.m, self.n)

    def get(self, x: Expr, y: Expr):
        # 获取第x行，第y列的元素，这里以1为开始序号
        x = simplify(x)
        y = simplify(y)
        if x.is_integer and y.is_integer:
            # 如果加正数假设，会不兼容字母参数，展示搁置
            ret = self.func.subs(self.x, x)
            ret = ret.subs(self.y, y)
            return ret
        else:
            raise Exception('args must be positive integer')

    def copy(self):
        ret = mn_matrix()
        ret.func = self.func
        ret.m = self.m
        ret.n = self.n
        ret.x = self.x
        ret.y = self.y
        return ret


class add_matrix(mn_matrix):
    '''
    定义矩阵加法运算
    '''

    def __init__(self, ma: mn_matrix, mb: mn_matrix) -> None:
        super().__init__()
        self.ma = ma.copy()
        self.mb = mb.copy()

    def get(self, x: Expr, y: Expr):
        return self.ma.get(x, y) + self.ma.get(x, y)

class scalar_mul_matrix(mn_matrix):
    '''
    定义矩阵数乘运算
    '''

    def __init__(self, mat: mn_matrix, k) -> None:
        super().__init__()
        self.mat = mat.copy()
        self.k = k

    def get(self, x: Expr, y: Expr):
        return sp.Mul(self.k, self.mat.get(x, y))