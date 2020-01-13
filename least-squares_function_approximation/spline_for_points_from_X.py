from spline_interpolation import *
from funcs import *
import matplotlib.pyplot as plt

points = list(get_file_points())
points = sorted(points, key=lambda x: x[0])
for i in points:
    plt.scatter(float(i[0]), float(i[1]), s=4, edgecolors="red")

x = [p[0] for p in points]
y = [p[1] for p in points]

spline = Spline_Interpolation(x,y)

interpolate = list(get_f_points(spline))

x = [p[0] for p in interpolate]
y = [p[1] for p in interpolate]

plt.title("Spline Interpolation based on 'X'")
plt.plot(x,y)
plt.xlim(-5, 6)
plt.ylim(-30,60)
plt.show()
