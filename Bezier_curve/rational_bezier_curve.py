from funcs import *
from bezier_curve import bezier_curve


"""
Rational Bezier Curve:
        
                ∑ (i=0;n) wi * Wi* B(n i)(t)  <----- bezier_curve(t)  | control points should be multiplied by weights before call bezier_curve(t)
        R(n) :=-----------------------------
                  ∑ (i=0;n) wi* B(n i)(t)     <----- sum_weights_mult_B(t)

where: 
    wi == i-th weight 
    Wi == i-th control point
    B(n i)(t) == Bernstein polynomial 
"""

class rational_bezier_curve:

    def __init__(self, points, weights):
        self.__n = len(points)-1
        self.__control_points =  [mult(weights[i], points[i]) for i in range(self.__n + 1) ]
        self.__weights = weights

    """call P(t) - rational bezier curve"""
    def __call__(self, t):
        curve = bezier_curve(self.__control_points)
        return curve(t)/self.sum_weights_mult_B(t)

    def sum_weights_mult_B(self, t):
        s = 0
        for i in range(len(self.__control_points)):
            s += self.__weights[i] * B(self.__n, i, t)
        return s