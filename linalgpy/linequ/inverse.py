from typing import List
import sympy as sp
from sympy.matrices.dense import MutableDenseMatrix
from linalgpy.core.solver import CoreSolver

class InverseSolver(CoreSolver):

    def __init__(self, mat: MutableDenseMatrix, evaluate=True) -> None:
        self.mat: MutableDenseMatrix = mat
        self.course: List[MutableDenseMatrix] = []
        self.invertible = False if self.mat.det() == 0 else True #可逆标志
        self.inv: MutableDenseMatrix = None # 存储计算结果的逆矩阵

        super().__init__(evaluate)

    def toExecute(self) -> None:
        if not self.invertible:
            raise Exception('矩阵不可逆')
        dim = self.mat.shape[0]
        mat = self.mat.copy()
        AE: MutableDenseMatrix = mat.row_join(sp.eye(dim)) #将原矩阵与单位矩阵连接，用Gauss-Jordan消元法求逆

        self.course.append(AE)
        #Gauss消元
        for pivot_rowInd in range(dim-1): #最后一行不用选主元
            pivot = AE[pivot_rowInd, pivot_rowInd]
            #选主元，如果待消元的列不为0，则选为主元，否则选最开始不为0的一行的元素为主元
            if pivot == 0:
                for rowInd in range(pivot_rowInd+1, dim):
                    if AE[rowInd, pivot_rowInd] != 0:
                        AE = AE.elementary_row_op(op="n<->m", row1=pivot_rowInd, row2=rowInd)
                        self.course.append(AE.copy())
                        break
            #用主元所在的行消元
            pivot = AE[pivot_rowInd, pivot_rowInd]
            for rowInd in range(pivot_rowInd+1, dim):
                if AE[rowInd, pivot_rowInd] != 0:
                    k = -sp.Pow(pivot, -1) * AE[rowInd, pivot_rowInd]
                    AE = AE.elementary_row_op(op='n->n+km', k=k, row1=rowInd, row2=pivot_rowInd)
                    self.course.append(AE.copy())

        #Jordan消元
        for pivot_rowInd in range(dim-1, 0, -1): #第一行不用选主元
            pivot = AE[pivot_rowInd, pivot_rowInd]
            #先将主元化为1
            if pivot != 1:
                AE = AE.elementary_row_op(op='n->kn', k=sp.Pow(pivot, -1), row=pivot_rowInd)
                self.course.append(AE.copy())
            #用主元所在的行消元
            for rowInd in range(pivot_rowInd-1, -1, -1): #这里-1不是倒叙，而是因为0的前一位是-1
                if AE[rowInd, pivot_rowInd] != 0:
                    k = -AE[rowInd, pivot_rowInd]
                    AE = AE.elementary_row_op(op='n->n+km', k=k, row1=rowInd, row2=pivot_rowInd)
                    self.course.append(AE.copy())

        #将第一行归一化
        if AE[0, 0] != 1:
            AE = AE.elementary_row_op(op='n->kn', k=sp.Pow(AE[0, 0], -1), row=0)
            self.course.append(AE.copy())

        self.inv = AE[:, int(AE.shape[1] / 2):]

    def toDict(self) -> dict:
        js = {}
        js['mat'] = sp.latex(self.mat)
        js['inv'] = sp.latex(self.inv)

        js['course'] = []
        for x in self.course:
            js['course'].append(sp.latex(x))
        return js


