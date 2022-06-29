# 极大线性无关组(MLIG) Maximal linearly independent group 

import sympy as sp
from linalgpy.linspace.lincombination import is_lincombination
from linalgpy.core.solver import CoreSolver

class MLIGSolver(CoreSolver):
    '''
    极大无关组求解器，注意为了兼容抽象的向量，构造方法中只能用列表装向量，不能直接用矩阵
    '''
    def __init__(self, group: list, evaluate=True) -> None:

        self.group: list = group
        self.coef: list = [] # 每次线性表示的系数
        self.MLIG: list = [] # 存储极大线性无关组
        self.position: list = [] # 存储极大线性无关组在group的位置

        super().__init__(evaluate)

    def toExecute(self) -> None:
        self.MLIG = [self.group[0]] # 请保证输入列表不为空
        self.position.append(0)
        for i in range(1, len(self.group)):
            coef = []
            flag = is_lincombination(self.MLIG, self.group[i], coef)
            self.coef.append(coef)
            if not flag:
                self.MLIG.append(self.group[i])
                self.position.append(i)

    def toDict(self) -> dict:
        js = {}
        js['position'] = self.position

        js['group'] = []
        for x in self.group:
            js['group'].append(sp.latex(x.T))

        js['coef'] = []
        for x in self.coef:
            coefI = []
            for y in x:
                coefI.append(sp.latex(y))
            js['coef'].append(coefI)

        return js
