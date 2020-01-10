import math
#            1- cos(x)
# lim 4038 * --------- = 2019
#              x^2
#
# De l'Hospital
# 
# 

def checkCOS():
    x = 1.0
    while math.cos(x) != 1.0:
        x /= 10
        print("cos(x) = ",math.cos(x),"\tx = ",x)

def f(x):
    return 4038 * (1-math.cos(x))/math.pow(x,2)

def task():
    x = 0.00000000001
    for i in range(11, 21):
        print("f(x) = ",f(x),"\tfor x = ",x)
        x/=10

print("experiment for task 1:")
task()
print("\n\nlet's check how cosinus works on 10^-i:\n")
checkCOS()