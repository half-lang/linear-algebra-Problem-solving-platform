from sympy import *
def readtext(str):
    str1=str[1:len(str)-1]
    str2 = []
    n = 0
    m = 0
    M=Matrix()
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
    str3=[]
    for i in range(len(str2)):
        str3.append(str2[i].split(sep=','))
    M=Matrix(str3)
    return M




