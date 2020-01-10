def foo(R):
    x = (3/(2*R) + 1/(2*R)) / 2 # to źle! 
    for i in range(0,5):
        x = x* (2 - x*R)
    return x

print(foo(-5))
print(foo(5))
print(foo(10))
print(foo(-10))
print(foo(100))
print(foo(-100))
print(foo(8))
print(foo(-8))
print(foo(2/3))
print(foo(3/2))
print(foo(1/10))