from funcs import *

"""
Bezier Curve:
        
        P(t) =  ∑ (i=0;n) wi * Wi* B(n i)(t)  <----- bezier_curve(t)  | control points should be multiplied by weights before call bezier_curve(t)
"""
class bezier_curve:

    def __init__(self, points):
        self.__control_points = points
        self.__n = len(points)-1

    """call P(t) - bezier curve"""
    def __call__(self, t):
        pnt = (0, 0)
        for i in range(0, self.__n+1):
            point = mult( B(self.__n, i, t), self.__control_points[i])
            pnt = plus(pnt, point)
        return pnt

    #""" rekursive calculate Points """
    #def __call__(self, t):
    #    return self.W(self.n, 0, t)

    #def W(self, n, k, t):
    #    if n==0: return self.__control_points[k]
    #    return plus(
    #                mult( 1-t, self.W(n-1, k, t) ), 
    #                mult( t, self.W(n-1, k+1, t) ))

"""Bernstein polynomials"""    
def B(n, k, x):
    return sp.binom(n,k) * x**k * (1 - x)**(n-k)