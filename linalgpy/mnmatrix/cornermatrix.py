from linalgpy.mnmatrix.mnmatrix import mn_matrix
from sympy import MutableDenseMatrix

class corner_matrix(mn_matrix):
    '''
    定义一个只知道四个角上的元素的矩阵，
    这里四个角上的元素可以不单是一个元素而是一个子矩阵。
    '''

    def __init__(self, tl, tr, bl, br, square=True) -> None:
        self.init_symbol() # 默认最后一行为第m行，最后一列为第n列，方阵则都是n
        self.tl: MutableDenseMatrix = tl # 左上角元素 top left
        self.tr: MutableDenseMatrix = tr # 右上角
        self.bl: MutableDenseMatrix = bl # 左下角 bottom left
        self.br: MutableDenseMatrix = br # 右下角

        if square: # 方阵标记
            self.m = self.n

        self.init_range()

    def init_range(self) -> None:
        # 生成可以查询的元素的范围
        self.tl_row = [i for i in range(1, self.tl.shape[0]+1)]
        self.tl_col = [i for i in range(1, self.tl.shape[1]+1)]

        self.tr_row = [i for i in range(1, self.tl.shape[1]+1)]
        self.tr_col = [self.n - i for i in range(self.tr.shape[0])]

        self.bl_row = [self.m - i for i in range(self.tr.shape[0])]
        self.bl_col = [i for i in range(1, self.tl.shape[1]+1)]

        self.br_row = [self.m - i for i in range(self.tr.shape[0])]
        self.br_col = [self.n - i for i in range(self.tr.shape[0])]

    def get(self, x, y):
        if x in self.tl_row and y in self.tl_col:
            return self.tl[x - 1, y - 1] # sympy原生的矩阵是以0开头的
        elif x in self.tr_row and y in self.tr_col:
            return self.tr[x - 1, y - self.n + self.tr.shape[0] - 1]
        elif x in self.bl_row and y in self.bl_col:
            return self.bl[x - self.m + self.tr.shape[1] - 1, y - 1]
        elif x in self.br_row and y in self.br_col:
            return self.br[x - self.m + self.tr.shape[1] - 1, y - self.n + self.tr.shape[0] - 1]
        else:
            return None