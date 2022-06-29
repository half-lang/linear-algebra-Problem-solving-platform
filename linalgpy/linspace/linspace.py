import sympy as sp
from sympy import MutableDenseMatrix, latex
from linalgpy.core.solver import CoreSolver
from linalgpy.linequ.gausslimination import GESolver 

class LinDependenceSolver(CoreSolver):
    '''
    判断向量组是否线性相关
    '''
    def __init__(self, mat: MutableDenseMatrix, evaluate=True) -> None:
        self.mat: MutableDenseMatrix = mat
        self.GES: GESolver = None
        self.result: bool = False # False表示线性无关
        super().__init__(evaluate)

    def toExecute(self) -> None:
        self.GES = GESolver(self.mat)
        if self.GES.result.rank() != self.mat.shape[1]:
            self.result = True

    def toDict(self) -> dict:
        js = {}
        js['mat'] = sp.latex(self.mat)
        js['GES'] = self.GES.dict()
        js['result'] = self.result
        return js

class BasisTransSolver(CoreSolver):
    #求基变换后线性映射的矩阵
    def __init__(self, mat: MutableDenseMatrix ,ma: MutableDenseMatrix, mb: MutableDenseMatrix, evaluate=True) -> None:
        self.ma: MutableDenseMatrix = ma # 变换前的基
        self.mb: MutableDenseMatrix = mb # 变换后的基
        self.mat: MutableDenseMatrix = mat # 变换前线性映射的矩阵
        self.result: MutableDenseMatrix = None # 变换后线性映射的矩阵
        self.matT: MutableDenseMatrix = None # 过渡矩阵
        super().__init__(evaluate)

    def toExecute(self) -> None:
        self.matT = self.ma @ self.mb.inv()
        self.result = self.matT.inv() @ self.mat @ self.matT

    def toDict(self) -> dict:
        js = {}
        js['ma'] = latex(self.ma)
        js['mb'] = latex(self.mb)
        js['mat'] = latex(self.mat)
        js['matT'] = latex(self.matT)
        js['result'] = latex(self.result)
        return js
