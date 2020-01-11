import csv
import matplotlib.pyplot as plt
from funcs import *

# points from X
for i in get_file_points(): 
    plt.scatter(float(i[0]), float(i[1]), s=4, edgecolors="red")
    print(i)

x = []
y = []
# points [ t, f(t) ]
for i in get_f_points(f):
    x.append(i[0])
    y.append(i[1])

plt.title("function 'f'")
plt.plot(x,y)
plt.xlim(-5, 6)
plt.ylim(-30,60)
plt.show()

