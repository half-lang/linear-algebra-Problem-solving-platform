from typing import Any, Callable, Tuple
from sympy.matrices.dense import MutableDenseMatrix
from lam.core.solver import matSolver, CoreSolver
from lam.metric import metricbase
from copy import copy

import sympy as sp
import logging
logging.basicConfig(level=logging.DEBUG)

class Schmidt_vector_orther(matSolver):
    '''
    专用于向量的Schmidt正交化求解器
    '''
    def __init__(self, mat: MutableDenseMatrix) -> None:
        super().__init__(mat)
        self.dim: tuple = mat.shape
        self.vecs: MutableDenseMatrix = sp.zeros(*self.dim)
        self.inns: MutableDenseMatrix = sp.zeros(*self.dim)
        self.course: Tuple[MutableDenseMatrix, MutableDenseMatrix] = []

    def get_course(self, is_norm = False) -> Tuple[MutableDenseMatrix, MutableDenseMatrix]:
        '''
        is_norm: 是否归一化，默认为False
        '''
        self.course = self.schmidt()
        if is_norm:
            self.normalize()
        return (self.vecs, self.inns)

    @staticmethod
    def compute_epsilon(i: int, mat: MutableDenseMatrix, vecs: MutableDenseMatrix, inns: MutableDenseMatrix):
        #仅用于中间过程的计算，返回的是每次计算出的一个正交基
        epsilon = mat[i, :]
        for j in range(i):
            epsilon = epsilon - sp.Mul(sp.Rational(inns[i, j], inns[j, j])) * vecs[j, :]
        return epsilon
        

    def schmidt(self) -> Tuple[MutableDenseMatrix, MutableDenseMatrix]:
        vecs, inns = sp.zeros(*self.dim), sp.zeros(*self.dim) # vecs存储正交化后的向量，inns存储内积
        row_num = self.dim[0]
        mat = self.mat

        for i in range(row_num):
            for j in range(i):
                inns[i, j] = metricbase.vector_inner(mat[i,:], vecs[j,:])
            vecs[i, :] = self.compute_epsilon(i, self.mat, vecs, inns)
            inns[i, i] = metricbase.vector_inner(vecs[i, :], vecs[i, :])

        self.vecs, self.inns = vecs, inns
        return (vecs, inns)

    def normalize(self):
        # 归一化正交化后的向量
        for i in range(self.dim[0]):
            self.vecs[i, :] = self.vecs[i, :] / self.vecs[i, :].norm()

class Schmidt_orther:
    '''
    泛用的Schmidt正交化求解器，支持向量，多项式的正交化
    inners的对角线元素存储(epsilon_i, epsilon_i), 下三角其他元素存储(alpha_i, epsilon_j)
    '''
    def __init__(self, data: list, inner: Callable[[Any, Any], Any]) -> None:
        self.data: list = data
        self.result: list = [0 for i in range(len(data))]
        self.inners: MutableDenseMatrix = sp.zeros(len(data))
        self.inner: Callable[[Any, Any], Any] = inner #定义data元素的内积函数

    def get_course(self) -> Tuple[list, MutableDenseMatrix]:
        self.schmidt()
        return (self.result, self.inners)

    def schmidt(self) -> None:
        row_num = len(self.data)
        for i in range(row_num):
            for j in range(i):
                self.inners[i, j] = self.inner(self.data[i], self.result[j])
            self.compute_epsilon(i)
            self.inners[i, i] = self.inner(self.result[i], self.result[i])

    def compute_epsilon(self, i: int) -> None:
        self.result[i] = copy(self.data[i])
        for j in range(i):
            # logging.debug(f'i:{i}, j:{j}')
            self.result[i] = self.result[i] - sp.Mul(self.inners[i, j] / self.inners[j, j]) * self.result[j]
    
class SchmidtVectorSolver(CoreSolver):
    '''
    适配于CoreSolver的Schmidt向量正交化求解器，矩阵的每一行代表一个向量
    inners的对角线元素存储(epsilon_i, epsilon_i), 下三角其他元素存储(alpha_i, epsilon_j)
    coef下三角元素存储(alpha_i, epsilon_j)/(epsilon_j, epsilon_j)
    '''
    def __init__(self, mat: MutableDenseMatrix, evaluate=True, normalize=True) -> None:
        self.mat: MutableDenseMatrix = mat
        self.normalize = normalize # 标记是否将结果单位化
        self.vecs: MutableDenseMatrix = sp.zeros(*mat.shape) # 存储存储正交化后的向量
        self.norm_vecs: MutableDenseMatrix = sp.zeros(*mat.shape) # 存储存储单位化后的向量
        self.inns: MutableDenseMatrix = sp.zeros(*mat.shape) # 存储计算过程中的内积
        self.coef: MutableDenseMatrix = sp.zeros(*mat.shape) # 存储计算过程中epsilon前的系数
        super().__init__(evaluate)

    def __compute_epsilon(self, i: int):
        '''
        仅用于中间过程的计算，返回的是每次计算出的一个正交基
        '''
        epsilon = self.mat[i, :]
        for j in range(i):
            self.coef[i, j] = sp.Mul(self.inns[i, j], sp.Pow(self.inns[j, j], -1))
            epsilon = epsilon - self.coef[i, j] * self.vecs[j, :]
        return epsilon

    def toExecute(self) -> None:
        mat = self.mat

        for i in range(mat.shape[0]):
            for j in range(i):
                self.inns[i, j] = metricbase.vector_inner(mat[i,:], self.vecs[j,:])

            self.vecs[i, :] = self.__compute_epsilon(i)
            self.inns[i, i] = metricbase.vector_inner(self.vecs[i, :], self.vecs[i, :])
        
        if self.normalize:
            for i in range(self.mat.shape[0]):
                self.norm_vecs[i, :] = self.vecs[i, :] / self.vecs[i, :].norm()

    def toDict(self) -> dict:
        js = {}

        js['mat'] = []
        for i in range(self.mat.shape[0]):
            js['mat'].append(sp.latex(self.mat[i, :].T))

        js['vecs'] = []
        for i in range(self.vecs.shape[0]):
            js['vecs'].append(sp.latex(self.vecs[i, :].T))

        js['norm_vecs'] = []
        for i in range(self.vecs.shape[0]):
            js['norm_vecs'].append(sp.latex(self.norm_vecs[i, :].T))

        js['coef'] = []
        for i in range(self.coef.shape[0]):
            coefI = []
            for j in range(self.coef.shape[1]):
                coefI.append(sp.latex(self.coef[i, j]))
            js['coef'].append(coefI)

        return js

