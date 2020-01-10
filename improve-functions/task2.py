import math

def sgn(x):
    if x == 0:
        return x
    return 1 if x > 0 else -1

def function(a, b, c):
    # f(x) = ax^2 + bx + c
    delta = pow(b, 2) - 4*a*c
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    return (x1, x2)

def better_function(a, b, c):
    # f(x) = ax^2 + bx + c
    delta = pow(b, 2) - 4*a*c
    x1 = (-b - (sgn(b) * math.sqrt(delta))) / (2*a)
    x2 = c/(a*x1)
    return (x1, x2)

print(function(1, 4, 4))
print(better_function(1, 4, 4))

print("\n")
print(function(1, 5, 6))
print(better_function(1, 5, 6))

print("\n")
print(function(pow(10,-17), 5, pow(10, -20)))
print(better_function(pow(10,-17), 5, pow(10, -20)))

print("\n")
print(function(pow(2,-17), 10, pow(2, -20)))
print(better_function(pow(2,-17), 10, pow(2, -20)))

print("\n")
print(function(pow(2,-30), 100, pow(2, -30)))
print(better_function(pow(2,-30), 100, pow(2, -30)))

