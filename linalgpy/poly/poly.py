from unittest import result
import sympy as sp
from sympy import MutableDenseMatrix, Symbol, latex
from linalgpy.core.solver import CoreSolver

class PolySolver(CoreSolver):
    '''
    计算矩阵多项式的值
    '''
    def __init__(self, mat: MutableDenseMatrix, var: Symbol, expr: sp.Expr, evaluate=True) -> None:
        self.mat: MutableDenseMatrix = mat # 矩阵的值
        self.var: Symbol = var # 定义主变量
        self.poly: sp.Poly = sp.Poly(sp.simplify(expr), var) # 关于矩阵的标量型多项式，注意必须用一次simplify，否则可能表达式会被视为一个整体

        self.matPoly: sp.MatrixExpr = None # 关于矩阵的矩阵型多项式
        self.subPoly: sp.MatrixExpr= None # 代入矩阵值的多项式
        self.result: MutableDenseMatrix = None # 矩阵多项式的值
        super().__init__(evaluate)

    def toExecute(self) -> None:
        coef = self.poly.all_coeffs()
        matVar = sp.MatrixSymbol('A', self.mat.shape[0], self.mat.shape[1])
        self.matPoly = (sp.Matrix(coef).T @ sp.Matrix([sp.MatPow(matVar, i) for i in range(len(coef)-1, -1, -1)]))[0]
        self.subPoly = self.matPoly.subs(matVar, self.mat)
        self.result = self.subPoly.as_explicit()

    def toDict(self) -> dict:
        js = {}
        js['mat'] = latex(self.mat)
        js['result'] = latex(self.result)
        js['matPoly'] = latex(self.matPoly)
        js['subPoly'] = latex(self.subPoly)
        return js


class SchmidtPolySolver(CoreSolver):
    '''
    适配于CoreSolver的Schmidt多项式正交化求解器
    '''
    def __init__(self, group: list, var: Symbol, evaluate=True, normalize=True) -> None:
        self.group: list = group # 待正交化的多项式组
        self.var: Symbol = var # 确定讨论的变量
        self.result: MutableDenseMatrix = list(range(len(group))) # 存储存储正交化后的多项式组
        self.unitized: MutableDenseMatrix = list(range(len(group))) # 存储存储单位化后的向量
        self.inns: MutableDenseMatrix = sp.zeros(len(group), len(group)) # 存储计算过程中的内积
        self.coef: MutableDenseMatrix = sp.zeros(len(group), len(group)) # 存储计算过程中epsilon前的系数
        self.normalize = normalize # 标记是否将结果单位化
        super().__init__(evaluate)

    @staticmethod
    def inner(a, b, x):
        return sp.integrate(a*b, (x, 0, 1)) # 定义多项式的内积

    def toExecute(self) -> None:
        group = self.group

        for i in range(len(group)):
            for j in range(i):
                self.inns[i, j] = self.inner(group[i], self.result[j], self.var)

            epsilon = group[i]
            for j in range(i):
                self.coef[i, j] = sp.Mul(self.inns[i, j], sp.Pow(self.inns[j, j], -1))
                epsilon = epsilon - self.coef[i, j] * self.result[j]
            self.result[i] = epsilon

            self.inns[i, i] = self.inner(self.result[i], self.result[i], self.var)
        
        if self.normalize:
            for i in range(len(group)):
                self.unitized[i] = self.result[i] / sp.sqrt(self.inns[i, i])

    def toDict(self) -> dict:
        js = {}
        js['group'] = list(map(latex, self.group))
        js['result'] = list(map(latex, self.result))
        js['unitized'] = list(map(latex, self.unitized))

        js['coef'] = []
        for i in range(self.coef.shape[0]):
            js['coef'].append(list(map(latex, self.coef[i, :])))

        return js