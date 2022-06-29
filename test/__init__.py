import sys
from pathlib import Path
lampy_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(lampy_dir))

import sympy as sp
from linalgpy.eigen.eigenvalue import EigenSolver

if __name__ == "__main__":
    mat = sp.Matrix([[1,2,2],[2,1,2],[2,2,1]])
    sol = EigenSolver(mat)
    m = sol.getEigenvectors()[1][2][0]
    print(sp.latex(m))

