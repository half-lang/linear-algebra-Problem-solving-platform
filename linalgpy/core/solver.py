from typing import List
from sympy.matrices.dense import MutableDenseMatrix

class matSolver:

    def __init__(self, mat: MutableDenseMatrix) -> None:
        self.mat: MutableDenseMatrix = mat
        self.course: List = []
        self.dim: int = mat.shape[0]

    def get_course(self) -> list:
        return self.course

class CoreSolver:

    def __init__(self, evaluate=True) -> None:
        self.evaluate = False
        if evaluate:
            self.execute()
            self.evaluate = True

    def execute(self) -> None:
        if not self.evaluate:
            self.toExecute()
            self.evaluate = True

    def toExecute(self) -> None:
        pass

    def dict(self) -> dict:
        if not self.evaluate:
            self.execute()
        return self.toDict()
    
    def toDict(self) -> dict:
        pass

    