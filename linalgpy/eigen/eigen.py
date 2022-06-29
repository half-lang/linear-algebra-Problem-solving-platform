from typing import List
import sympy as sp
from sympy import MutableDenseMatrix, Poly, latex
from sympy.abc import lamda
from linalgpy.core.solver import CoreSolver

class EigenValueSolver(CoreSolver):
    # 求解特征值
    def __init__(self, mat: MutableDenseMatrix, evaluate=True) -> None:
        self.mat: MutableDenseMatrix = mat
        self.charpoly: Poly = None
        self.lambda_mat: MutableDenseMatrix = None
        self.result: List = []
        super().__init__(evaluate)

    def toExecute(self) -> None:
        self.lambda_mat = sp.eye(self.mat.shape[0])*lamda - self.mat
        self.charpoly = sp.factor(self.mat.charpoly()) # factor用于做整数的分解
        self.result = self.mat.eigenvals()

    def toDict(self) -> dict:
        js = {}
        js['mat'] = latex(self.mat)
        js['charpoly'] = latex(self.charpoly.args[0])
        js['lambda_mat'] = latex(self.lambda_mat).replace('left[', 'left|').replace('right]', 'right|')
        js['result'] = []
        for x in list(self.result.items()):
            js['result'].append(list(map(latex, x)))

        return js

class EigenVectorSolver(CoreSolver):
    # 求解特征向量
    def __init__(self, mat: MutableDenseMatrix, evaluate=True) -> None:
        self.mat: MutableDenseMatrix = mat
        self.EVAS: EigenValueSolver = None # 存储一个特征值求解器
        self.result: List = []
        self.equ_mat: List = []
        super().__init__(evaluate)

    def toExecute(self) -> None:
        self.EVAS = EigenValueSolver(self.mat)
        self.result = self.mat.eigenvects()
        for x in self.result:
            self.equ_mat.append(self.EVAS.lambda_mat.subs(lamda, x[0]))
    
    def toDict(self) -> dict:
        js = {}
        js['mat'] = latex(self.mat)
        js['EVAS'] = self.EVAS.dict()

        js['equ_mat'] = []
        for x in list(self.equ_mat):
            js['equ_mat'].append(latex(x))

        js['result'] = []
        for x in list(self.result):
            js['result'].append(list(map(latex, x[2])))

        return js

