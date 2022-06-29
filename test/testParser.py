import sys
from pathlib import Path
lampy_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(lampy_dir))

from latex.parser import matParser
from linalgpy.linequ.gausslimination import GESolver

mat = matParser("[[a, 1, 1, 1],[1, a, 1, a],[1, 1, a, a^2]]")
print(mat)
# so = GESolver(mat)
# print(so.dict())

