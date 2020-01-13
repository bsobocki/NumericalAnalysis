from funcs import *
from bezier_curve import *
import matplotlib.pyplot as plt

# get points sorted in ascending order
points = list(get_file_points())
points = sorted(points, key=lambda x: x[0])

# draw points
for i in points:
    plt.scatter(float(i[0]), float(i[1]), s=4, edgecolors="red")

# create a new bezier curve
P = bezier_curve(points)

# get points from bezier_curve
curve = [P(h) for h in t(1000)] 

# add points to plot
x = [p[0] for p in curve]
y = [p[1] for p in curve]

plt.title("Bezier Curve based on 'X'")
plt.plot(x, y)
plt.show()