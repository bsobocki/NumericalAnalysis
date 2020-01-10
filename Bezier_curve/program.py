from draw_curve import *
import matplotlib.pyplot as plt

points = [(0,0), (3.5, 36), (25, 25), (25, 1.5), (-5, 3), (-5, 33), (15, 11), (-0.5, 35), (19.5, 15.5), (7, 0), (1.5, 10.5)]
weights1 = [1, 6, 4, 2, 3, 4, 2, 1, 5, 4, 1]
weights2 = [1, 3, 2, 1, 1, 2, 1, 1, 2, 2, 1]
weights3 = [1,   12,   4, 2, 3, 4, 2, 1,   15,   4, 1]


# --- Bezier Curve --- #

fig = plt.figure(figsize=(10,10))
xlim = (-10, 100)
ylim = (-10, 200)

fig.add_subplot(1, 3, 1)
draw_bezier_curve(points, weights1)
plt.xlim(xlim)
plt.ylim(ylim)

fig.add_subplot(1, 3, 2)
draw_bezier_curve(points, weights2)
plt.xlim(xlim)
plt.ylim(ylim)

fig.add_subplot(1, 3, 3)
draw_bezier_curve(points, weights3)
plt.xlim(xlim)
plt.ylim(ylim)

plt.show()


# --- Rational Bezier Curve --- #

fig = plt.figure(figsize=(10,10))
xlim = (-10, 40)
ylim = (-10, 40)

fig.add_subplot(1, 3, 1)
draw_rational_bezier_curve(points, weights1)
plt.xlim(xlim)
plt.ylim(ylim)

fig.add_subplot(1, 3, 2)
draw_rational_bezier_curve(points, weights2)
plt.xlim(xlim)
plt.ylim(ylim)

fig.add_subplot(1, 3, 3)
draw_rational_bezier_curve(points, weights3)
plt.xlim(xlim)
plt.ylim(ylim)

plt.show()