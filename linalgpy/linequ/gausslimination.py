from typing import List
import sympy as sp
from sympy import MutableDenseMatrix, latex
from linalgpy.core.solver import CoreSolver
        

class GESolver(CoreSolver):
    '''
    执行高斯消元法的求解器
    '''
    def __init__(self, mat: MutableDenseMatrix, evaluate=True) -> None:
        self.mat: MutableDenseMatrix = mat
        self.course: List[MutableDenseMatrix] = []
        self.result: MutableDenseMatrix = None
        super().__init__(evaluate)


    def toExecute(self) -> None:
        mat: MutableDenseMatrix = self.mat.copy()
        for pivot_rowInd in range(min(mat.shape)): #行消元次数取决行数小还是列数小
            #选主元，如果待消元的列不为0，则选为主元，否则选最开始一行的元素为主元
            pivot = mat[pivot_rowInd, pivot_rowInd]
            if pivot == 0:
                for rowInd in range(pivot_rowInd+1, mat.shape[0]):
                    if mat[rowInd, pivot_rowInd] != 0:
                        mat = mat.elementary_row_op(op="n<->m", row1=pivot_rowInd, row2=rowInd)
                        self.course.append(mat.copy())
                        break
            #用主元所在的行消元
            pivot = mat[pivot_rowInd, pivot_rowInd]
            for rowInd in range(pivot_rowInd+1, mat.shape[0]):
                if mat[rowInd, pivot_rowInd] != 0:
                    k = -sp.Mul(mat[rowInd, pivot_rowInd], sp.Pow(pivot, -1))
                    mat = mat.elementary_row_op(op='n->n+km', k=k, row1=rowInd, row2=pivot_rowInd)
                    self.course.append(mat.copy())
        self.result = self.course[-1]

    def toDict(self) -> dict:
        # 返回该对象latex文本化的字典对象      
        js = {}
        js['course'] = list(map(latex, self.course))
        js['mat'] = latex(self.mat)
        js['result'] = latex(self.result)

        return js
