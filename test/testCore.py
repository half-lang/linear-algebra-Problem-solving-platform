import __init__
from linalgpy.core.solver import CoreSolver

class MySolver(CoreSolver):
    
    def __init__(self, evaluate=True) -> None:
        print('__init__')
        super().__init__(evaluate)

    def toDict(self):
        print('__to_dict')

    def toExecute(self):
        print('__execute')

if __name__ == "__main__":
    solver = MySolver(evaluate=False)
    solver.execute()
    solver.execute()
    solver.dict()
    solver.dict()