from typing import List, Tuple
from sympy import MutableDenseMatrix, Expr, latex, simplify
from linalgpy.core.solver import CoreSolver
from linalgpy.linequ.gausslimination import GESolver


# 重写行列式展开
class DeterminantSolver(CoreSolver):
    
    def __init__(self, mat: MutableDenseMatrix, evaluate=True) -> None:
        self.mat: MutableDenseMatrix = mat
        self.course: List[List[Tuple[Expr, MutableDenseMatrix]]] = [] # 保存化到三阶行列式之前的过程
        self.result: List = [] # 保存每个三阶行列式的结果
        self.sum: Expr = None # 将每个三阶行列式的结果求和
        super().__init__(evaluate)

    def toExecute(self) -> None:
        mat: MutableDenseMatrix = self.mat.copy()

        self.course.append([(1, mat)])
        for i in range(mat.shape[0]-3):
            ls = []
            for c, m in self.course[-1]:
                ls.extend(self.rowExpansion(c, m))
            self.course.append(ls)

        for c, m in self.course[-1]:
            self.result.append(simplify(c*m.det()))

        self.sum = simplify(sum(self.result))

    @staticmethod
    def rowExpansion(coef: Expr, mat: MutableDenseMatrix):
        ls: List[Tuple[Expr, MutableDenseMatrix]] = []
        for ind in range(mat.shape[1]):
            ls.append((simplify(mat[0, ind]*coef*(-1)**ind), mat.minor_submatrix(0, ind)))
        return ls

    def toDict(self) -> dict:
        js = {}
        js['mat'] = latex(self.mat).replace('left[', 'left|').replace('right]', 'right|')
        js['sum'] = latex(self.sum)

        js['coef'] = [] # 存储余子式之前的系数
        js['cofactor'] = [] # 存储余子式
        js['operater'] = [] # 存储余子式之间的加号或减号
        for row in self.course:
            coef_ls = []
            cofactor_ls = []
            operater_ls = []
            for c, m in row:
                cofactor_ls.append(latex(m).replace('left[', 'left|').replace('right]', 'right|'))
                if latex(c)[0] == '-': # 去除多余的符号
                    latexc = latex(c)[1:]
                    operater_ls.append('-')
                else:
                    latexc = latex(c)
                    operater_ls.append('+')
                if latexc == '1': # 去除多余的系数1
                    latexc = ''
                coef_ls.append(latexc)
            js['coef'].append(coef_ls)
            js['cofactor'].append(cofactor_ls)
            js['operater'].append(operater_ls)

        js['result'] = []
        js['result_operater'] = []
        for x in self.result:
            if latex(x)[0] == '-':
                js['result'].append(latex(x)[1:])
                js['result_operater'].append('-')
            else:
                js['result'].append(latex(x))
                js['result_operater'].append('+')

        return js

# 高斯消元求行列式
class GausseDeterminantSolver(CoreSolver):

    def __init__(self, mat: MutableDenseMatrix, evaluate=True) -> None:
        self.mat: MutableDenseMatrix = mat
        self.GES: GESolver = None # 存储一个高斯消元法的求解器
        self.result_mat = None # 存储化为阶梯型的矩阵
        self.result = 1 # 存储行列式值
        super().__init__(evaluate)

    def toExecute(self) -> None:
        self.GES = GESolver(self.mat)
        self.result_mat = self.GES.course[-1]
        for i in range(self.result_mat.shape[0]):
            self.result *= self.result_mat[i,i]

    def toDict(self) -> dict:
        js = {}
        js['GES'] = self.GES.dict()
        js['result'] = latex(self.result)
        
        js['factor'] = []
        for i in range(self.result_mat.shape[0]):
            js['factor'].append(latex(self.result_mat[i,i]))

        return js