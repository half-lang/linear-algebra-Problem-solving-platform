import copy
import sympy as sp
from sympy import MutableDenseMatrix, symbols, latex
from typing import List
from linalgpy.core.solver import CoreSolver



def __is_matrix_lincombination(group: List, vect: MutableDenseMatrix, coef: list = []) -> bool:
    '''
    判断vect是否是group的线性组合，专用于数字向量。
    '''
    num = len(group)

    group = copy.deepcopy(group) #重新把列表group构造成矩阵
    for i in range(len(group)):
        group[i] = list(group[i])
    group = sp.Matrix(group).T 
    
    flag = False
    vars = [] # 创建未知元，用以求解方程
    for i in range(num):
        vars.append(symbols(f"x{i}"))
    res = sp.linsolve((group, vect), vars)

    if isinstance(res, sp.sets.sets.EmptySet):
        return flag
    else:
        flag = True
        for x in res.args[0]: #res是有限集，其参数可以被迭代器调用
            for i in range(num):
                x = x.subs(vars[i], 0)
            coef.append(x)
        return flag
        

def is_lincombination(group: List, vect, coef: List = []) -> bool:
    '''
    判断vect是否是group的线性组合，coef作为引用参数用于返回线性组合的系数
    '''
    flag = False
    if isinstance(vect, MutableDenseMatrix):
        flag = __is_matrix_lincombination(group, vect, coef)
    return flag


class LincombinationSolver(CoreSolver):
    # 对象化的判断线性组合的求解器
    def __init__(self, mat: MutableDenseMatrix, vec: MutableDenseMatrix, evaluate=True) -> None:
        self.mat: MutableDenseMatrix = mat # 线性组合的向量组
        self.vec: MutableDenseMatrix = vec # 被判断的向量
        self.solveset = None # 解方程时的解集
        self.coef: List = [] # 线性组合的系数
        super().__init__(evaluate)

    def toExecute(self) -> None:
        vars = [] # 创建未知元，用以求解方程
        for i in range(self.mat.shape[1]):
            vars.append(symbols(f"x{i}"))
        self.solveset = sp.linsolve((self.mat, self.vec), vars)

        if self.solveset.is_empty:
            self.solveset = []
        else:
            for x in self.solveset.args[0]:
                for i in range(self.mat.shape[1]):
                    x = x.subs(vars[i], 0)
                self.coef.append(x)
        

    def toDict(self) -> dict:
        js = {}
        js['mat'] = latex(self.mat)
        js['vec'] = latex(self.vec)
        js['coef'] = list(map(latex, self.coef))
        js['solveset'] = list(map(latex, self.solveset.args[0]))
        ind = 0
        for x in js['coef']: # 处理负号的连接问题，为有负号的字符串加括号
            if x[0] == '-':
                js['coef'][ind] = f'({x})'
            ind += 1

        return js