import sympy as sp
from sympy import MutableDenseMatrix, latex
from linalgpy.core.solver import CoreSolver
from linalgpy.eigen.eigen import EigenVectorSolver
import logging

logging.basicConfig(level=logging.WARN)

class DiagSymmetricSolver(CoreSolver):
    # 对称矩阵对角化
    def __init__(self, mat: MutableDenseMatrix, evaluate=True) -> None:
        self.mat: MutableDenseMatrix = mat
        self.matT: MutableDenseMatrix = sp.eye(mat.shape[0]) # 过渡矩阵
        self.matD: MutableDenseMatrix = sp.eye(mat.shape[0]) # 对角化的矩阵
        self.EVES: EigenVectorSolver = None # 存储一个特征向量的求解器
        super().__init__(evaluate)

    def toExecute(self) -> None:
        self.EVES = EigenVectorSolver(self.mat)
        ind = 0
        for x in self.EVES.result:
            for y in x[2]:
                self.matD[ind, ind] = x[0]
                self.matT[:, ind] = y
                ind += 1
    
    def toDict(self) -> dict:
        js = {}
        js['mat'] = latex(self.mat)
        js['matT'] = latex(self.matT)
        js['matD'] = latex(self.matD)
        js['EVES'] = self.EVES.dict()
        return js