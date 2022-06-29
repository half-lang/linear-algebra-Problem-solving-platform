from typing import List
import sympy as sp
from sympy import MutableDenseMatrix, latex
from linalgpy.linequ.gausslimination import GESolver

class LinequSolver:
    '''
    线性方程组Ax = b的求解器
    '''
    def __init__(self, mat: MutableDenseMatrix, vec: MutableDenseMatrix, evaluate=True) -> None:

        self.mat: MutableDenseMatrix = mat # 方程左端的矩阵A
        self.vec: MutableDenseMatrix = vec # 方程右端的常数项b
        self.Ab: MutableDenseMatrix = sp.Matrix.hstack(mat, vec) # A和b构成的扩增矩阵[A,b]
        self.elimination_course: List[MutableDenseMatrix] = [] # 存储阶梯化矩阵的过程
        self.solveset: tuple = () # 存储方程的解集

        # 不需要输出的字段
        self.GES: GESolver = None
        self.evaluate = False # 标记是否已经求解

        if evaluate:
            self.get_course()
            self.evaluate = True

    
    def get_course(self) -> None:
        if not self.evaluate:
            self.reduce_row()
            self.solve_echelon()

    def reduce_row(self) -> None:
        '''
        先进行矩阵阶梯化运算
        '''
        self.GES = GESolver(self.Ab)
        self.elimination_course = self.GES.course
        self.Ab = self.elimination_course[-1]

    def solve_echelon(self) -> None:
        '''
        解出reduce_row(self)得到的阶梯型矩阵
        '''
        self.solveset = sp.linsolve(self.Ab)
        if self.solveset.is_empty: # 如果解集为空，solveset就是空列表
            self.solveset = ()
        else:
            self.solveset =  self.solveset.args[0]

    def dict(self):
        if not self.evaluate:
            self.get_course()

        js = {}
        js['mat'] = latex(self.mat)
        js['vec'] = latex(self.vec)
        js['Ab'] = latex(self.Ab)
        js['elimination_course'] = self.GES.dict()['course']

        js['solveset'] = []
        for x in self.solveset:
            js['solveset'].append(latex(x))
        js['solveset'] = tuple(js['solveset'])

        self.js = js
        return self.js
        
