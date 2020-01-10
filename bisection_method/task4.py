import math
from bisection import *

def f(x):
    return pow(x,2) - 2*x - math.atan(7*x - 2)

alpha1 = 0.225333477
_range = (0, 1)
print(bisection(f, _range, alpha1))

alpha2 = 2.58389241
_range = (2, 3)
print(bisection(f, _range, alpha2))