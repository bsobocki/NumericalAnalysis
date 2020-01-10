import scipy.special as sp

"""Bernstein polynomials"""    
def B(n, k, x):
    return sp.binom(n,k) * x**k * (1 - x)**(n-k)


""" arguments generator """
def t(n):
    for i in range (0, n+1):
        yield i/(n)


""" scalar mult point """
def mult(a, point):
    return (a*point[0], a*point[1])


""" point plus point """ 
def plus(point_a, point_b):
    return (point_a[0] + point_b[0], point_a[1] + point_b[1])