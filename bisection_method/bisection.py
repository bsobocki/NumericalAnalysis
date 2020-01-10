import math

def sign(a):
    return 0 if a==0 else -1 if a<0 else 1

def alpha_between_A_B(_fun, _A, _B):
    return sign(_fun(_A))*sign(_fun(_B)) < 0

def bisection_print(_fun, _range, _alpha, _N):
    a = _range[0]
    b = _range[1]
    for i in range(0, _N):
        m = (a+b)/2
        print("alpha = ",_alpha,"\tm = ",m,"\tf(m)= ",_fun(m),"\t| e | =  ", abs(_alpha - m))
        if alpha_between_A_B(_fun, a, m):
            b = m
        else:
            a = m

def bisection(_fun, _range, _alpha):
    a = _range[0]
    b = _range[1]
    m = 0
    while abs(_fun(m)) >= 0.00001:
        m = (a+b)/2
        if alpha_between_A_B(_fun, a, m):
            b = m
        else:
            a = m
    return m