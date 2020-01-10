import math
from bisection import *

def f(x):
    return x * math.exp(-x) - 0.06064

alpha = 0.0646926359947960
a0 = 0
b0 = 1
_range = (a0, b0)
bisection(f, _range, alpha, 15)