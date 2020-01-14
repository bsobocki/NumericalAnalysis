from l_s_aprox import l_s_aprox as lsa
import random as ran
import matplotlib.pyplot as plt

def f(x):
    return x + 4

def results(f, start=0, end=5):
    res = []
    while start <= end:
        start += 0.1
        res.append(f(start))
    return res

def results_with_errors(f, start=0, end=5):
    res = []
    while start <= end: 
        r = ran.uniform(0, 1)
        start += 0.1
        res.append([start, f(start)+r])
    return res

res = results(f)
res_err = results_with_errors(f)

# linear function
aprox = lsa(2, res_err)

x = [x/10 for x in range(0, 51)]
y = [aprox(xx) for xx in x]

plt.plot(x, res)
plt.plot(x,y)
plt.show()