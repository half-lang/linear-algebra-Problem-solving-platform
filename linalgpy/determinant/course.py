import sympy as sp
from sympy.matrices.expressions.matadd import MatAdd

from linalgpy.determinant import laplaceexpand
from linalgpy.core.matrixexpression import decompose_mono


def det_course(matrix: sp.MatrixBase):
    '''
    det_course函数接受矩阵对象的参数，并将返回一个存储矩阵表达式的字典，键'expand'表示行列式的展开过程，它的值是一个列表，列表的每个元素都是矩阵对象；键'figure'表示行列式展开到三阶后直接求值的过程，它的值是个列表，每个元素存储的都是矩阵表达式。列表中的数学元素都可以用latex函数打印。
    '''
    course = {}
    course['expand'] = lap_expand_course(matrix)
    expr = course['expand'][-1]
    course['figure'] = detpoly_figure_course(expr)
    return course

def lap_expand_course(matrix: sp.MatrixBase):
    time = matrix.shape[0] - 3  #三阶以内不展开
    expr = matrix
    course = [0 for i in range(time + 1)]
    course[0] = matrix
    for i in range(time):
        expr = laplaceexpand.lapexp_expr(expr)
        course[i+1] = expr
    return course

def detpoly_figure_course(expr: MatAdd):
    course = []
    expr_list = []
    laplaceexpand.read_mat_mono(expr_list, expr)
    for ind in range(len(expr_list)):
        dic = decompose_mono(expr_list[ind])
        expr_list[ind] = sp.Mul(dic['coe'], dic['mat'].det())
    course.append(sp.Add(*expr_list, evaluate = False))
    course.append(course[-1].doit())
    return course
