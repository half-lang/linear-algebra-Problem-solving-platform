import logging
import sympy as sp
from sympy.matrices.dense import MutableDenseMatrix, eye

logging.basicConfig(level=logging.DEBUG)

def is_complete_square(mat: MutableDenseMatrix, i: int) -> bool:
    #判断平方项a_{ii}是否已经配方
    flag = True
    for k in range(mat.shape[0]):
        if k != i and mat[i, k] != 0:
            flag = False
            break
    return flag
    

def quad_term_trans(mat: MutableDenseMatrix, i: int) -> MutableDenseMatrix:
    # 配方平方项的线性变数替换，i表示平方项的下标
    dim = mat.shape[0]
    ret: MutableDenseMatrix = sp.eye(dim)
    for k in range(dim):
        if k != i:
            ret[i, k] = -sp.Mul(sp.Pow(mat[i, i], -1), mat[i, k])
    return ret

def cross_term_trans(mat: MutableDenseMatrix, i: int , j:int) -> MutableDenseMatrix:
    # 消去交叉项的线性变数替换，i，j表示交叉项的下标a_{ij}
    if i == j:
        raise Exception("不是交叉项")
    ret: MutableDenseMatrix = sp.eye(mat.shape[0])
    ret[i,i], ret[j,j], ret[i,j], ret[j,i] = 1, -1, 1, 1
    return ret

def next_quad_op(mat: MutableDenseMatrix) -> MutableDenseMatrix:
    #找到对mat进行下一步标准化操作的变换
    if mat.is_symmetric() == False:
        raise Exception('不是对称矩阵')

    dim: int = mat.shape[0]
    for i in range(dim):
        if is_complete_square(mat, i) == False and mat[i,i] != 0:
            return quad_term_trans(mat, i), 'quad'
    
    for i in range(dim):
        for j in range(dim):
            if mat[i,j] != 0 and i != j:
                return cross_term_trans(mat, i, j), 'cross'
    
    return eye(dim), 'none'

if __name__ == "__main__":
    mat = sp.Matrix([
        [1,3,4],
        [3,2,3],
        [4,3,7],
    ])
    tra = next_quad_op(mat)
    logging.debug(tra)
    mat = tra.T @ mat @ tra
    logging.debug(mat)
    tra = next_quad_op(mat)
    logging.debug(tra)
    mat = tra.T @ mat @ tra
    logging.debug(mat)
