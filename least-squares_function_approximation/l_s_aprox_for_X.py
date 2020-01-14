from l_s_aprox import *
from funcs import *
import matplotlib.pyplot as plt

def approx(degree):
    # draw points
    for i in points: plt.scatter(float(i[0]), float(i[1]), s=4, edgecolors="red")

    lsa = l_s_aprox(degree, points)

    # get points from bezier_curve
    curve = list(get_f_points(lsa)) 

    x = [p[0] for p in curve]
    y = [p[1] for p in curve]

    plt.title("W*"+str(degree-1)+" for 'X'")
    plt.xlim(-5, 6)
    plt.ylim(-30,60)
    plt.plot(x, y)
    plt.show()



points = list(get_file_points())

#approx(2)
#approx(3)
#approx(4)
#approx(5)
#approx(6)
#approx(26)
approx(30)