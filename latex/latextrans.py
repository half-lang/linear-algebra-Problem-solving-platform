import sympy as sp
from sympy.abc import *
from sympy.parsing.latex import parse_latex
##用于将文本文件转换为sympy公式、目前开发的只包括矩阵形式的latex公式。但对于线性代数求解已经可以满足基本情况。其中对{}的识别较差##
escape_dict = \
    {
        '\a': r'\a', '\b': r'\b', '\c': r'\c', '\f': r'\f', '\n': r'\n', '\r': r'\r', '\t': r'\t', '\v': r'\v',
               '\'': r'\'', '\"': r'\"', '\0': r'\0', '\1': r'\1', '\2': r'\2', '\3': r'\3', '\4': r'\4', '\5': r'\5',
               '\6': r'\6', '\7': r'\7', '\8': r'\8', '\9': r'\9','\\':r'\\'

     }


def raw(text):
    """Returns a raw string representation of text"""
    new_string = ''
    for char in text:
        try: new_string += escape_dict[char]
        except KeyError: new_string += char
    return new_string
def latextrans(formula:str):
    try:
        formula=formula.split('{matrix}')[1]
        formula=formula.split('\end')[0]
        formula=formula.split(r'\\')[0:-1]
        matrix=[]
        for i in range(len(formula)):
            matrix.append(formula[i].split('&'))
        result=matrix
        return result
    except:
        str=formula
        str1 = str[1:len(str) - 1]
        str2 = []
        n = 0
        m = 0
        while (n <= len(str1)):
            while n <= len(str1) and str1[n] != ']':
                n += 1
            while str1[m] != '[' and m < n:
                m += 1
            if m != n:
                str2.append(str1[m + 1:n])
            m += 1
            n += 1
            if n == len(str1):
                break
        str3 = []
        for i in range(len(str2)):
            str3.append(str2[i].split(sep=','))
        return str3
def standard_transformation(matrix:list):
    result=[]
    for i in range(len(matrix)):
        result.append([])
        for j in range(len(matrix[0])):
            result[i].append(parse_latex(matrix[i][j]))
    result=sp.Matrix(result)
    return result
def strtrans(formula:str):
    return standard_transformation(latextrans(formula))
if __name__ == '__main__':
    print(standard_transformation(latextrans(r'[[1, 2, 3], [3.3, \sqrt{\frac{\eta}{\sqrt{\eta}}}, 1.3], [7, 11, 32]]')))
    print(standard_transformation(latextrans(r'\left[ \begin{matrix}1&2&3\\3.3&	\sqrt{\frac{\eta}{\sqrt{\eta}}}&1.3\\7&	11&	32\\\end{matrix} \right] ')))