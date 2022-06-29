# 讨论含单个参数的线性方程组

from typing import List, Tuple
import sympy as sp
from sympy import MutableDenseMatrix, Symbol, Expr, latex
from linalgpy.linequ.linequsolver import LinequSolver
from linalgpy.core.solver import CoreSolver


class LambdaLinSolver(CoreSolver):

    def __init__(self, mat: MutableDenseMatrix, lam: Symbol, evaluate=True) -> None:
        '''
        求解含单个参数的线性方程组的求解器，
        设线性方程组为AX = b，参数mat代表其增广矩阵(A, b)，
        默认evaluate = True，即构造求解器后立即执行求解。
        '''
        self.mat: MutableDenseMatrix = mat # 给定一个待求解的增广矩阵
        self.mA: MutableDenseMatrix = mat[:, :-1] # 线性方程组的系数矩阵A
        self.mb: MutableDenseMatrix = mat[:, -1] # 线性方程组的常数项
        self.determinat: Expr = None # A的行列式计算出的多项式
        self.factorization: Expr = None # self.determinat的因式分解式
        self.root: Tuple[Expr] = None # 保留多项式self.determinat的根
        self.LQS_list: List[LinequSolver] = [] # 行列式为0时，解线性方程的过程(LinequSolver = LQS)
        self.LQS_nozero: LinequSolver = None # 行列式不为0时，解线性方程的过程
        self.lam: Symbol = lam # 用于告知求解器方程中参数的字母符号，比如lambda字母对应sympy.abc.lambda对象
        self.rank: List = [] # 行列式为0时，解线性方程系数矩阵与增广矩阵的秩

        super().__init__(evaluate)

    def toExecute(self) -> None:
        self.determinat = self.mA.det()
        self.factorization = sp.factor(self.determinat)
        self.root = sp.solveset(self.determinat)

        if self.root.is_empty:
            self.root = ()
        else: # 如果self.determinat有实根(默认实数)，则讨论行列式等于0的情况
            self.root = self.root.args
            for rt in self.root:
                self.LQS_list.append(LinequSolver(self.mA.subs(self.lam, rt), self.mb.subs(self.lam, rt)))
                self.rank.append((self.mA.subs(self.lam, rt).rank(), self.mat.subs(self.lam, rt).rank()))

        # 行列式不等于0的情况
        self.LQS_nozero = LinequSolver(self.mA, self.mb)

    def toDict(self) -> dict:
        js = {}
        js['mat'] = latex(self.mat)
        js['mA'] = latex(self.mA)
        js['mb'] = latex(self.mb)
        js['determinat'] = latex(self.determinat)
        js['factorization'] = latex(self.factorization)
        js['lam'] = latex(self.lam)
        js['rank'] = self.rank
        
        js['root'] = []
        for rt in self.root:
            js['root'].append(sp.latex(rt))
        js['root'] = tuple(js['root'])
        
        js['LQS_list'] = []
        for x in self.LQS_list:
            js['LQS_list'].append(x.dict())

        js['LQS_nozero'] = self.LQS_nozero.dict()


        return js

