import math


####### a #######

def f_a(x):
    return 4*pow(math.cos(x), 2) - 3

def f_a2(x):
    s = 1
    for i in range (1, 76):
        sign = (-1, 1)[i%2==0]
        s += sign*pow(2, 2*i+1)*pow(x, 2*i)/math.factorial(2*i)
    return s

def f_a3(x):
    return 4*(1 - pow(math.sin(x),2)) - 3

def f_a4(x):
    s = 4 * math.cos(x) - 3
    for i in range(1, 76):
        sign = (-1, 1)[i%2==0]
        s += sign*4*math.cos(x)*pow(x, 2*i)/math.factorial(2*i)
    return s

def f_a5(x):
    return math.cos(3*x)*math.cos(x)



####### b #######

def f_b1(x):
    return math.log(x, 5) - 6

def f_b2(x):
    return math.log(x/pow(5, 6), 5)


print("\n-------- a --------\n")

print("\n1/6 * pi")
print(f_a(math.pi/6))
print(f_a2(math.pi/6))
print(f_a3(math.pi/6))
print(f_a4(math.pi/6))
print(f_a5(math.pi/6))


print("\n11/6 * pi")
print(f_a(11/6 * math.pi))
print(f_a2(11/6 * math.pi))
print(f_a3(11/6 * math.pi))
print(f_a4(11/6 * math.pi))
print(f_a5(11/6 * math.pi))

print("\n7/6 * pi")
print(f_a(7/6 *math.pi))
print(f_a2(7/6 *math.pi))
print(f_a3(7/6 *math.pi))
print(f_a4(7/6 *math.pi))
print(f_a5(7/6 *math.pi))

print("\n pi")
print(f_a(math.pi))
print(f_a2(math.pi))
print(f_a3(math.pi))
print(f_a4(math.pi))
print(f_a5(math.pi))

print("\n-------- b --------\n")

print(f_b1(pow(5,6)))
print(f_b2(pow(5,6)))