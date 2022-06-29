import sympy as sp
'''
矩阵中公式的处理/将矩阵中多项式转换为列表储存。
'''
def decompose_mono(matexpr) -> dict:
    '''
    把矩阵单项式拆分成系数和矩阵
    '''
    dic = {'coe':1, 'mat':0}
    if isinstance(matexpr, sp.MatrixBase):
        dic['mat'] = matexpr
        return dic
    else:
        for x in matexpr.args:
            if isinstance(x, sp.MatrixBase):
                dic['mat'] = x
            else:
                dic['coe'] = x
        return dic