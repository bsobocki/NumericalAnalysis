import scipy.special as sp
import csv

def f(t):
    return (t + 3.6) * (t - 2.1) * (t - 3.7)

def get_f_points(f, start=-6.0, end=6.0):
    while start <= end: 
        if not start == 0:
            yield [start, f(start)]
        start += 0.01

def get_file_points(source='punkty.csv'):
    with open(source, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for i in reader:
            yield [float(i[0]), float(i[1])]

"""Bernstein polynomials"""    
def B(n, k, x):
    return sp.binom(n,k) * x**k * (1 - x)**(n-k)

""" arguments generator """
def t(n):
    for i in range (0, n+1):
        yield i/(n)


""" scalar mult point """
def mult(a, point):
    return (a * point[0], a * point[1])


""" point plus point """ 
def plus(point_a, point_b):
    return (point_a[0] + point_b[0], point_a[1] + point_b[1])