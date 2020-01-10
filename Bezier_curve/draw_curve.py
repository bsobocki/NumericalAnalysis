from bezier_curve import bezier_curve
from rational_bezier_curve import rational_bezier_curve
import bezier_curve as b_c
import matplotlib.pyplot as plt

def draw_curve(P, points):
    curve = [P(h) for h in b_c.t(1000)] 

    x = [p[0] for p in curve]
    y = [p[1] for p in curve]

    # draw curve
    p = plt.plot(x,y)

    xp = [p[0] for p in points]
    yp = [p[1] for p in points]

    # draw points
    for i in points:
        plt.scatter(i[0], i[1], s=2, color=p[0].get_color())

    # draw lines between given points
    plt.plot(xp, yp,linewidth=0.2,  color=p[0].get_color())

def draw_bezier_curve(points, weights):
    plt.title("Bezier Curve")
    points = [b_c.mult(weights[i],points[i]) for i in range(len(points))]

    # function described bezier curve for given points
    P = bezier_curve(points)

    draw_curve(P, points)


def draw_rational_bezier_curve(points, weights):
    plt.title("Rational Bezier Curve")
    P = rational_bezier_curve(points, weights)

    draw_curve(P, points)