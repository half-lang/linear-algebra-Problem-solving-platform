import sympy as sp
from sympy.matrices.expressions.matadd import MatAdd


'''
实现Laplace展开的模块
有矩阵的表达式，请用MatAdd,MatMul实现加和乘
'''

def lap_expand(matrix, n: int = 0, coe = 1, axis: int = 0):
    #axis   0表示按行展开，否则按列展开
    expr = _lap_expr_0(matrix, n, coe) if axis == 0 else _lap_expr_1(matrix, n, coe)
    return expr

def _lap_expr_0(matrix, n: int = 0, coe = 1):
    #按行展开函数的实现
    expr, startInd = _lap_init_expr_0(matrix, n, coe)
    for colInd in range(startInd+1 ,matrix.shape[1]):
        if matrix[n, colInd] == 0:
            t = sp.MatMul(coe*matrix[n, colInd]*(-1)**(n+colInd), matrix.minor_submatrix(n, colInd), evaluate = True)
        else:
            t = sp.MatMul(coe*matrix[n, colInd]*(-1)**(n+colInd), matrix.minor_submatrix(n, colInd), evaluate = False)
        if not isinstance(t, sp.matrices.expressions.special.ZeroMatrix):
            expr = sp.MatAdd(expr, t, evaluate = False)
    return expr
    
def _lap_init_expr_0(matrix, n: int = 0, coe = 1):
    #用于初始化按行展开的表达式
    expr = 0
    startInd = 0
    for colInd in range(matrix.shape[1]):
        if matrix[n, colInd] == 0: #去掉一些不必要的系数如0，使得输出格式化，-1是必要的因为元素是行列式不是乘法
            expr = sp.MatMul(coe*matrix[n, colInd]*(-1)**(n+colInd), matrix.minor_submatrix(n, colInd), evaluate = True)
        else:
            expr = sp.MatMul(coe*matrix[n, colInd]*(-1)**(n+colInd), matrix.minor_submatrix(n, colInd), evaluate = False)
        if not isinstance(expr, sp.matrices.expressions.special.ZeroMatrix):    #hint 0矩阵不等于0，不能用==判别
            startInd = colInd
            break
    return (expr, startInd)

def _lap_expr_1(matrix, n: int = 0, coe = 1):
    expr, startInd = _lap_init_expr_1(matrix, n)
    for rowInd in range(startInd+1 ,matrix.shape[0]):
        if matrix[rowInd, n] == 0:
            t = sp.MatMul(coe*matrix[rowInd, n]*(-1)**(n+rowInd), matrix.minor_submatrix(rowInd, n), evaluate = True)
        else:
            t = sp.MatMul(coe*matrix[rowInd, n]*(-1)**(n+rowInd), matrix.minor_submatrix(rowInd, n), evaluate = False)
        if not isinstance(t, sp.matrices.expressions.special.ZeroMatrix):
            expr = sp.MatAdd(expr, t, evaluate = False)
    return expr

def _lap_init_expr_1(matrix, n: int = 0, coe = 1):
    expr = 0
    startInd = 0
    for rowInd in range(matrix.shape[1]):
        if matrix[rowInd, n] == 0: 
            expr = sp.MatMul(coe*matrix[rowInd, n]*(-1)**(n+rowInd), matrix.minor_submatrix(rowInd, n), evaluate = True)
        else:
            expr = sp.MatMul(coe*matrix[rowInd, n]*(-1)**(n+rowInd), matrix.minor_submatrix(rowInd, n), evaluate = False)
        if not isinstance(expr, sp.matrices.expressions.special.ZeroMatrix):    #hint 0矩阵不等于0，不能用==判别
            startInd = rowInd
            break
    return (expr, startInd)

def lap_exp_mono(expr, n: int = 0, axis: int = 0):  
    '''
    矩阵单项式的Laplace展开
    expr    是系数乘矩阵的一个单项式
    '''
    if isinstance(expr, sp.MatrixBase):
        # print(type(expr))
        return lap_expand(expr, n = n, axis = axis)
    coe = 1
    for x in expr.args:
        if isinstance(x, sp.MatrixBase):
            expr = x
        else:
            coe = x
    return lap_expand(expr, coe = coe)

def lapexp_expr(expr):
    '''
    输入为表达式的Laplace展开函数，它兼容矩阵形式的参数输入
    expr: MatrixBaser/Expr
    '''
    if isinstance(expr, sp.MatrixBase):
        return lap_expand(expr)
    args = []
    read_mat_mono(args, expr)
    expr_list = [0 for i in range(len(args))]
    for i in range(len(args)):
        expr_list[i] = lap_exp_mono(args[i])
    expr = sp.MatAdd(*expr_list)
    return expr

def read_mat_mono(args: list, poly: sp.Expr) -> None:
    '''
    读取矩阵多项式的单项式
    Parameter:
        args 用于存储读取的单项式，作为隐式的返回
        poly: 被读取的多项式，兼容单项式
    '''
    if not isinstance(poly, MatAdd):
        args.append(poly)
        return
        
    for x in poly.args:
        if isinstance(x, MatAdd):
            read_mat_mono(args, x)
        else:
            args.append(x)
    return
    
