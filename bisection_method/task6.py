import math

def foo(a):
    x = (math.sqrt(5/(3*a)) + 1/math.sqrt(3*a)) /2
    for i in range(0,5):
        x = x* (1.5 - 0.5*a*x*x)
    return x

print(foo(100))
print(foo(16))
print(foo(1))
print(foo(4))
print(foo(81))
print(foo(36))
print(foo(pow(2/3, 2)))