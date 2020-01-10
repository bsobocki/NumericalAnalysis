import math

def f(x):
    x11 = pow(x, 11.0)
    return 4038 * (math.sqrt(x11 + 1) - 1) / x11

def better_f(x):
    return 4038 / (math.sqrt(pow(x, 11.0) + 1) + 1)

print("given function: f(x)\nf(0.01) = ", f(0.01))
print("\nimproved function: better_f(x)\n better_f(0.01) = ", better_f(0.01))