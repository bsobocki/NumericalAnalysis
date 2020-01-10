import math
#       f(x+h)-f(x)
# lim  -------------
#            h
def normalDerivative(f, x, h):
    return ( f(x+h) - f(x) ) / h

#        f(x+h) - f(x-h)
#  lim  ----------------
#              2h
def anotherDerivative(f, x, h):
    return ( f(x+h) - f(x-h) ) / (2*h)

def checkDerivatives(f, x):
    h = pow(2,-5)
    for i in range(1, 30):
        h /= 2
        der1 = normalDerivative(f, x, h)
        der2 = anotherDerivative(f, x, h)
        print("i = ",-(i+5),"der1: ",der1,"\tder2: ",der2,"\t|der1-der2| = ",der1-der2)

print("f(x) = 100*x^2 | f'(x) = 200x\nx = 10\nf'(10.0025) = 2000")
checkDerivatives(lambda x : 100*pow(x,2), 10.0025)

print("\nf(x) = 3x^3 - x | f'(x) = 9x^2 - 1\nx = 1/3\nf'(1/3) = 0")
checkDerivatives(lambda x: pow(x,3) - x, 1/3)

print("\nf(x) = 300*sin(x) | f'(x) = 300cos(x)\nx = PI\nf'(PI) = -300")
checkDerivatives(lambda x : 300 * math.sin(x), math.pi)

print("\nf(x) = x^5 + 4x^3 + 7x^2 + 1 | f'(x) = 5x^4 + 12x^2 + 14x \nf'(100)=")
checkDerivatives(lambda x : pow(x,5) + pow(x,3)*4 + pow(x,2)*7 + 1, 100)

print("\nf(x) = tg(x)")
checkDerivatives(lambda x : math.tan(x), math.pi/2)

print("\nf(x) = cos(x) + e*ln(x) | f'(x) = -sin(x) + (pi/2)/x")
checkDerivatives(lambda x : math.cos(x) + (math.pi/2)*math.log(x, math.e), math.pi/2)