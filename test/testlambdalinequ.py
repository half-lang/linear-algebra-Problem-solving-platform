import __init__
import sympy as sp
from sympy.abc import a
from sympy import S, sqrt, RR
from linalgpy.linequ import lambdalinequ, linequsolver

def traverse_list(js, key):
    ind = 0
    for value in js:
        if isinstance(value, dict):
            traverse_dict(value, key)
        else:
            print(f'{key}{ind}: {value}')
        ind += 1


def traverse_dict(js, dictkey):
    print(f'dictkey: {dictkey}')
    for key in js:
        if isinstance(js[key], dict):
            traverse_dict(js[key], dictkey)
        elif isinstance(js[key], list):
            traverse_list(js[key], key)
        else:
            print(f'{key}: {js[key]}')

def testFactor():
    mat = [
        [a, 1, 1],
        [1, a, 1],
        [1, 1, a],
    ]
    mat = sp.Matrix(mat)
    deter = mat.det()
    print(deter)
    # sset = sp.solveset(deter)
    # print(sset)
    fd = sp.factor(a**2 + 2, domain=RR)
    print(fd)

def testSubs():
    mat = [
        [a, 1, 1],
        [1, a, 1],
        [1, 1, a],
    ]
    mat = sp.Matrix(mat)
    print(mat.subs(a, 2))


def testLinequjson():
    mat = [
        [a, 1, 1],
        [1, a, 1],
        [1, 1, a],
    ]
    vec = [
        [1],
        [a],
        [a**2],
    ]
    mat = sp.Matrix(mat)
    vec = sp.Matrix(vec)
    solver = linequsolver.LinequSolver(mat, vec)
    print(solver.solveset)
    print(solver.dict()['solveset'])
    print(sp.latex(solver.solveset[0]))
    js = []
    for x in solver.solveset:
        js.append(sp.latex(x))
    print(js[0])

def testlambdalinequDict():
    mat = [
        [a, 1, 1, 1],
        [1, a, 1, a],
        [1, 1, a, a**2],
    ]
    mat = sp.Matrix(mat)
    solver = lambdalinequ.LambdaLinSolver(mat, a)
    print(solver.dict())

def testRank():
    mat = [
        [a, 1, 1, 1],
        [1, a, 1, a],
        [1, 1, a, a**2],
    ]
    mat = sp.Matrix(mat)
    print(mat.rank())
    print(mat[:,:-1].rank())


if __name__ == "__main__":
    testRank()