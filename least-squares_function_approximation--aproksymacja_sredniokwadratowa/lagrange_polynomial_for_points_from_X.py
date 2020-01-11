from lagrange_polynomial_interpolation import Lagrange_Polynomial_Interpolation as LPI
from funcs import *
import matplotlib.pyplot as plt

points = list(get_file_points())
for i in points:
    plt.scatter(float(i[0]), float(i[1]), s=4, edgecolors="red")

interp = LPI(points)
points = list(get_f_points(interp))
xs = [x[0] for x in points] 
ys = [x[1] for x in points] 

plt.plot(xs, ys)
plt.title("Efekt Rungego")
plt.xlim(-5, 6)
plt.ylim(-30,60)
plt.show()